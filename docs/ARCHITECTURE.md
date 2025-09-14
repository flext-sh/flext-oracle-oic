# FLEXT Oracle OIC - Architecture Guide

**Clean Architecture + Domain-Driven Design for Oracle Integration Cloud**

## Table of Contents

- [Overview](#overview)
- [Clean Architecture Implementation](#clean-architecture-implementation)
- [Domain-Driven Design Patterns](#domain-driven-design-patterns)
- [FLEXT Ecosystem Integration](#flext-ecosystem-integration)
- [Enterprise Architecture Principles](#enterprise-architecture-principles)
- [Layer Responsibilities](#layer-responsibilities)
- [Design Patterns](#design-patterns)
- [Architecture Decision Records](#architecture-decision-records)

## Overview

**FLEXT Oracle OIC** implements Clean Architecture with Domain-Driven Design patterns specifically optimized for Oracle Integration Cloud Gen3 APIs. This architecture ensures:

- **Separation of Concerns**: Clear boundaries between business logic and infrastructure
- **Testability**: Each layer can be tested independently with real Oracle OIC APIs
- **Maintainability**: Changes to external services don't impact business logic
- **Scalability**: Asyncio-native architecture for high-performance integration
- **Enterprise Patterns**: Implementation of proven Enterprise Integration Patterns

## Clean Architecture Implementation

### Architecture Layers (Dependency Rule)

```
┌─────────────────────────────────────────┐
│           Interface Layer               │
│  ┌─────────────────────────────────────┐│
│  │        Application Layer            ││
│  │  ┌─────────────────────────────────┐││
│  │  │         Domain Layer            │││
│  │  │   ┌─────────────────────────┐   │││
│  │  │   │    Business Entities   │   │││
│  │  │   └─────────────────────────┘   │││
│  │  │   ┌─────────────────────────┐   │││
│  │  │   │    Domain Services      │   │││
│  │  │   └─────────────────────────┘   │││
│  │  └─────────────────────────────────┘││
│  │  ┌─────────────────────────────────┐││
│  │  │      Use Cases/Commands         │││
│  │  └─────────────────────────────────┘││
│  └─────────────────────────────────────┘│
│  ┌─────────────────────────────────────┐│
│  │        Infrastructure Layer        ││
│  │   (Oracle OIC APIs, External)      ││
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
```

### Dependency Rule Enforcement

- **Inner layers** never depend on outer layers
- **Domain Layer** has no dependencies on external libraries
- **Application Layer** depends only on Domain abstractions
- **Infrastructure Layer** implements Domain interfaces
- **Interface Layer** orchestrates Application services

## Domain-Driven Design Patterns

### Strategic Patterns

#### **Bounded Context: Oracle OIC Integration**

```python
# Domain Boundaries
from flext_oracle_oic.domain import (
    # Core Integration Context
    OICIntegration,
    WorkflowProcess,
    MessagePattern,
    IntegrationResult,

    # Authentication Context
    OICConnection,
    AuthToken,
    IdentityProvider,

    # WMS Integration Context
    WMSAdapter,
    WarehouseOperation,
    InventorySync
)
```

#### **Ubiquitous Language**

| Domain Term | Definition | Implementation |
|-------------|------------|----------------|
| **Integration** | Complete Oracle OIC workflow execution | `OICIntegration` entity |
| **Pattern** | Enterprise Integration Pattern execution | `MessagePattern` entity |
| **Adapter** | Oracle OIC pre-built connector | `WMSAdapter` value object |
| **Flow** | Oracle OIC integration sequence | `WorkflowProcess` entity |
| **Routing** | Message routing based on content | `MessageRouter` service |
| **Scatter-Gather** | Parallel processing pattern | `ScatterGatherPattern` service |

### Tactical Patterns

#### **Entities (Business Identity)**

```python
from dataclasses import dataclass
from typing import List, Optional
from flext_core import FlextResult

@dataclass
class OICIntegration:
    """Core integration entity with business identity."""

    integration_id: str
    name: str
    status: IntegrationStatus
    patterns: List[MessagePattern]
    created_at: datetime

    def execute_pattern(self, pattern_name: str, input_data: dict) -> FlextResult[PatternResult]:
        """Execute specific integration pattern."""
        pattern = self._find_pattern(pattern_name)
        if not pattern:
            return FlextResult.fail(f"Pattern {pattern_name} not found")

        return pattern.execute(input_data)

    def _find_pattern(self, name: str) -> Optional[MessagePattern]:
        return next((p for p in self.patterns if p.name == name), None)

@dataclass
class WorkflowProcess:
    """Long-running business process entity."""

    process_id: str
    name: str
    steps: List[WorkflowStep]
    state: ProcessState

    def advance_to_next_step(self) -> FlextResult[WorkflowStep]:
        """Advance workflow to next step."""
        current_step = self._get_current_step()
        if current_step.is_complete:
            next_step = self._get_next_step()
            if next_step:
                self.state = self.state.transition_to(next_step.state)
                return FlextResult.ok(next_step)

        return FlextResult.fail("Cannot advance workflow")
```

#### **Value Objects (Business Values)**

```python
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass(frozen=True)
class OICConnectionInfo:
    """Oracle OIC connection information value object."""

    base_url: str
    region: str
    oauth_config: OAuthConfig

    def __post_init__(self):
        if not self.base_url.startswith('https://'):
            raise ValueError("OIC URL must use HTTPS")

    def to_client_config(self) -> Dict[str, Any]:
        return {
            'base_url': self.base_url,
            'region': self.region,
            'auth': self.oauth_config.to_dict()
        }

@dataclass(frozen=True)
class AuthToken:
    """Authentication token value object."""

    access_token: str
    token_type: str = "Bearer"
    expires_in: int = 3600
    scope: Optional[str] = None

    def is_expired(self) -> bool:
        return self._issued_at + timedelta(seconds=self.expires_in) < datetime.now()

    def to_header(self) -> Dict[str, str]:
        return {"Authorization": f"{self.token_type} {self.access_token}"}
```

#### **Domain Services (Business Logic)**

```python
from abc import ABC, abstractmethod
from flext_core import FlextResult

class IntegrationPatternEngine:
    """Domain service for pattern execution logic."""

    def __init__(self):
        self._patterns: Dict[str, PatternExecutor] = {}

    def register_pattern(self, name: str, executor: PatternExecutor):
        """Register new integration pattern."""
        self._patterns[name] = executor

    def execute_pattern(
        self,
        pattern_name: str,
        message: dict,
        context: IntegrationContext
    ) -> FlextResult[PatternResult]:
        """Execute integration pattern with business validation."""

        # Business rule: Validate pattern exists
        if pattern_name not in self._patterns:
            return FlextResult.fail(f"Unknown pattern: {pattern_name}")

        # Business rule: Validate message structure
        validation_result = self._validate_message(message, pattern_name)
        if validation_result.is_failure:
            return FlextResult.fail(f"Message validation failed: {validation_result.error}")

        # Execute pattern
        executor = self._patterns[pattern_name]
        return executor.execute(message, context)

    def _validate_message(self, message: dict, pattern_name: str) -> FlextResult[None]:
        """Apply business rules for message validation."""
        required_fields = self._get_required_fields(pattern_name)

        for field in required_fields:
            if field not in message:
                return FlextResult.fail(f"Missing required field: {field}")

        return FlextResult.ok(None)

class WorkflowOrchestrator:
    """Domain service for workflow management."""

    def __init__(self, pattern_engine: IntegrationPatternEngine):
        self._pattern_engine = pattern_engine

    def execute_workflow(
        self,
        workflow: WorkflowProcess,
        input_data: dict
    ) -> FlextResult[WorkflowResult]:
        """Execute complete workflow with business orchestration."""

        result_data = input_data.copy()

        for step in workflow.steps:
            # Execute step pattern
            step_result = self._pattern_engine.execute_pattern(
                step.pattern_name,
                result_data,
                step.context
            )

            if step_result.is_failure:
                return FlextResult.fail(f"Workflow step {step.name} failed: {step_result.error}")

            # Merge step results for next step
            result_data.update(step_result.unwrap().data)

        return FlextResult.ok(WorkflowResult(
            workflow_id=workflow.process_id,
            status="completed",
            final_data=result_data
        ))
```

#### **Repository Interfaces (Data Access Abstraction)**

```python
from abc import ABC, abstractmethod
from typing import List, Optional
from flext_core import FlextResult

class IntegrationRepository(ABC):
    """Abstract repository for integration persistence."""

    @abstractmethod
    async def save(self, integration: OICIntegration) -> FlextResult[str]:
        """Save integration configuration."""
        pass

    @abstractmethod
    async def find_by_id(self, integration_id: str) -> FlextResult[Optional[OICIntegration]]:
        """Find integration by ID."""
        pass

    @abstractmethod
    async def find_by_status(self, status: IntegrationStatus) -> FlextResult[List[OICIntegration]]:
        """Find integrations by status."""
        pass

    @abstractmethod
    async def delete(self, integration_id: str) -> FlextResult[bool]:
        """Delete integration."""
        pass

class WorkflowRepository(ABC):
    """Abstract repository for workflow persistence."""

    @abstractmethod
    async def save_process(self, process: WorkflowProcess) -> FlextResult[str]:
        """Save workflow process."""
        pass

    @abstractmethod
    async def find_active_processes(self) -> FlextResult[List[WorkflowProcess]]:
        """Find all active workflow processes."""
        pass

    @abstractmethod
    async def update_process_state(
        self,
        process_id: str,
        new_state: ProcessState
    ) -> FlextResult[bool]:
        """Update workflow process state."""
        pass
```

## FLEXT Ecosystem Integration

### Zero Custom Implementation Policy

**FLEXT Oracle OIC** leverages the complete FLEXT ecosystem without custom implementations:

#### **flext-core Integration**

```python
# Foundation patterns from flext-core
from flext_core import (
    FlextResult,           # Railway-oriented programming
    FlextDomainService,    # Domain service base class
    FlextContainer,        # Dependency injection
    get_logger            # Structured logging
)

class OracleOICService(FlextDomainService[OICRequest, OICResponse]):
    """Main Oracle OIC service using FLEXT patterns."""

    def __init__(self):
        super().__init__()
        self._logger = get_logger("oracle_oic_service")
        self._container = FlextContainer.get_global()

    async def execute(self, request: OICRequest) -> FlextResult[OICResponse]:
        """Execute Oracle OIC integration with FLEXT patterns."""
        self._logger.info(f"Processing OIC request: {request.integration_name}")

        # Use FLEXT dependency injection
        pattern_engine = self._container.get(IntegrationPatternEngine)
        auth_service = self._container.get(AuthenticationService)

        # Railway-oriented programming with FlextResult
        return await (
            auth_service.authenticate(request.auth_config)
            .bind(lambda auth: pattern_engine.execute_pattern(
                request.pattern_name,
                request.data,
                auth
            ))
            .map(lambda result: OICResponse(
                integration_id=request.integration_id,
                result=result,
                status="success"
            ))
        )
```

#### **flext-api Integration**

```python
# HTTP abstractions from flext-api
from flext_api import (
    FlextHttpClient,      # HTTP client abstraction
    FlextApiGateway,      # API gateway patterns
    FlextRequestContext   # Request context management
)

class OracleOICApiClient:
    """Oracle OIC API client using FLEXT abstractions."""

    def __init__(self, config: OracleOICConfig):
        # Use FLEXT HTTP client (no direct httpx)
        self._http_client = FlextHttpClient(
            base_url=config.base_url,
            timeout=config.request_timeout,
            retry_config=config.retry_config
        )

    async def call_oic_api(
        self,
        endpoint: str,
        data: dict,
        context: FlextRequestContext
    ) -> FlextResult[dict]:
        """Call Oracle OIC API using FLEXT abstractions."""

        response_result = await self._http_client.post(
            endpoint=endpoint,
            json=data,
            context=context
        )

        if response_result.is_failure:
            return FlextResult.fail(f"OIC API call failed: {response_result.error}")

        return FlextResult.ok(response_result.unwrap().json())
```

#### **flext-auth Integration**

```python
# Authentication from flext-auth
from flext_auth import (
    FlextAuth,            # Authentication orchestrator
    AuthToken,            # Token management
    FlextAuthConfig       # Auth configuration
)

class OracleIDCSAuthenticator:
    """Oracle IDCS authentication using FLEXT auth patterns."""

    def __init__(self, idcs_config: IDCSConfig):
        # Use FLEXT authentication (no custom OAuth2)
        auth_config = FlextAuthConfig(
            provider="oracle_idcs",
            client_id=idcs_config.client_id,
            client_secret=idcs_config.client_secret,
            token_url=idcs_config.token_url
        )

        self._flext_auth = FlextAuth(auth_config)

    async def authenticate(self) -> FlextResult[AuthToken]:
        """Authenticate with Oracle IDCS using FLEXT patterns."""
        return await self._flext_auth.oauth2_client_credentials_flow()
```

## Enterprise Architecture Principles

### 1. Railway-Oriented Programming

**Every operation returns `FlextResult[T]` for safe error propagation:**

```python
async def process_integration_workflow(
    integration_name: str,
    input_data: Dict[str, Any]
) -> FlextResult[IntegrationResult]:
    """
    Complete integration workflow using railway-oriented programming.
    Each step can fail safely without exceptions.
    """

    # Chain operations with automatic error propagation
    return await (
        # Step 1: Validate integration configuration
        validate_integration_config(integration_name)

        # Step 2: Authenticate with Oracle OIC (only if step 1 succeeds)
        .bind(lambda config: authenticate_oracle_oic(config))

        # Step 3: Execute integration pattern (only if step 2 succeeds)
        .bind(lambda auth: execute_integration_pattern(auth, input_data))

        # Step 4: Monitor execution (only if step 3 succeeds)
        .bind(lambda result: monitor_integration_execution(result))

        # Step 5: Transform result (only if step 4 succeeds)
        .map(lambda monitoring: IntegrationResult(
            status="completed",
            data=monitoring.final_data,
            execution_time=monitoring.duration
        ))
    )

# Individual steps also use FlextResult
async def validate_integration_config(name: str) -> FlextResult[IntegrationConfig]:
    """Validate integration configuration."""
    config_result = await load_integration_config(name)

    if config_result.is_failure:
        return FlextResult.fail(f"Config loading failed: {config_result.error}")

    config = config_result.unwrap()

    # Business validation
    if not config.is_valid():
        return FlextResult.fail(f"Invalid configuration: {config.validation_errors}")

    return FlextResult.ok(config)
```

### 2. Dependency Inversion Principle

**Depend on abstractions, not implementations:**

```python
# High-level policy (Application Layer)
class IntegrationOrchestrator:
    """High-level integration orchestration."""

    def __init__(
        self,
        # Depend on abstractions (interfaces)
        integration_repo: IntegrationRepository,      # Not concrete implementation
        pattern_engine: IntegrationPatternEngine,     # Not specific pattern executor
        auth_service: AuthenticationService,          # Not Oracle IDCS specifically
        oic_client: OracleOICClient                   # Not httpx client
    ):
        self._integration_repo = integration_repo
        self._pattern_engine = pattern_engine
        self._auth_service = auth_service
        self._oic_client = oic_client

# Low-level details (Infrastructure Layer)
class PostgreSQLIntegrationRepository(IntegrationRepository):
    """Concrete implementation of integration repository."""

    async def save(self, integration: OICIntegration) -> FlextResult[str]:
        # PostgreSQL-specific implementation
        pass

class OracleOICGen3Client(OracleOICClient):
    """Concrete implementation of Oracle OIC client."""

    async def call_integration_api(self, endpoint: str, data: dict) -> FlextResult[dict]:
        # Oracle OIC Gen3-specific implementation
        pass

# Dependency Injection Configuration
def configure_dependencies(container: FlextContainer):
    """Configure dependency injection."""
    container.register(IntegrationRepository, PostgreSQLIntegrationRepository)
    container.register(OracleOICClient, OracleOICGen3Client)
    container.register(IntegrationOrchestrator, IntegrationOrchestrator)
```

### 3. Single Responsibility Principle

**Each class has one reason to change:**

```python
# ✅ GOOD: Single responsibility classes

class MessageValidator:
    """Validates message content and structure."""

    def validate(self, message: dict, pattern_type: str) -> FlextResult[None]:
        # Only validates messages - single responsibility
        pass

class PatternExecutor:
    """Executes integration patterns."""

    def execute(self, pattern: MessagePattern, message: dict) -> FlextResult[PatternResult]:
        # Only executes patterns - single responsibility
        pass

class IntegrationLogger:
    """Logs integration events."""

    def log_execution(self, integration_id: str, result: PatternResult) -> None:
        # Only handles logging - single responsibility
        pass

class IntegrationService:
    """Orchestrates integration execution."""

    def __init__(
        self,
        validator: MessageValidator,
        executor: PatternExecutor,
        logger: IntegrationLogger
    ):
        # Composes single-responsibility components
        self._validator = validator
        self._executor = executor
        self._logger = logger
```

## Layer Responsibilities

### Domain Layer (Inner Core)

**Responsibilities:**
- Core business entities and value objects
- Domain services with business logic
- Repository interfaces (abstractions)
- Domain events and business rules

**Dependencies:**
- **NONE** - Pure business logic
- Only standard Python libraries
- No external framework dependencies

```python
# Domain Layer - Pure business logic
class IntegrationPattern:
    """Core domain entity for integration patterns."""

    def __init__(self, name: str, rules: List[RoutingRule]):
        # Pure business logic - no external dependencies
        self._name = name
        self._rules = rules

    def can_process_message(self, message: dict) -> bool:
        """Business rule: Check if pattern can process message."""
        return any(rule.matches(message) for rule in self._rules)
```

### Application Layer (Use Cases)

**Responsibilities:**
- Application services and use cases
- Command and query handlers
- Application-specific business flows
- Coordination of domain services

**Dependencies:**
- Domain layer only
- FLEXT core abstractions
- Repository interfaces (not implementations)

```python
# Application Layer - Use cases and coordination
from flext_core import FlextResult, get_logger

class ExecuteIntegrationCommand:
    """Command handler for integration execution."""

    def __init__(
        self,
        integration_repo: IntegrationRepository,    # Domain interface
        pattern_engine: IntegrationPatternEngine    # Domain service
    ):
        self._integration_repo = integration_repo
        self._pattern_engine = pattern_engine
        self._logger = get_logger("execute_integration")

    async def handle(self, command: ExecuteIntegrationRequest) -> FlextResult[IntegrationResult]:
        """Handle integration execution use case."""

        # Load integration (domain operation)
        integration_result = await self._integration_repo.find_by_id(command.integration_id)
        if integration_result.is_failure:
            return FlextResult.fail(f"Integration not found: {command.integration_id}")

        integration = integration_result.unwrap()

        # Execute pattern (domain service)
        execution_result = self._pattern_engine.execute_pattern(
            command.pattern_name,
            command.message,
            command.context
        )

        if execution_result.is_failure:
            self._logger.error(f"Pattern execution failed: {execution_result.error}")
            return FlextResult.fail(execution_result.error)

        return FlextResult.ok(IntegrationResult(
            integration_id=command.integration_id,
            pattern_result=execution_result.unwrap(),
            status="completed"
        ))
```

### Infrastructure Layer (External Concerns)

**Responsibilities:**
- Oracle OIC API clients
- Database implementations
- External service integrations
- Framework-specific implementations

**Dependencies:**
- All layers
- External libraries (httpx, asyncpg, etc.)
- Oracle OIC APIs
- Third-party services

```python
# Infrastructure Layer - External service implementations
import httpx
from flext_core import FlextResult

class OracleOICRestClient(OracleOICClient):
    """Concrete Oracle OIC API client implementation."""

    def __init__(self, config: OracleOICConfig):
        self._base_url = config.base_url
        self._auth_token = None
        self._http_client = httpx.AsyncClient(
            base_url=config.base_url,
            timeout=config.timeout
        )

    async def call_integration_api(
        self,
        endpoint: str,
        data: dict
    ) -> FlextResult[dict]:
        """Call Oracle OIC REST API."""
        try:
            response = await self._http_client.post(
                endpoint,
                json=data,
                headers=self._get_auth_headers()
            )
            response.raise_for_status()
            return FlextResult.ok(response.json())
        except httpx.HTTPError as e:
            return FlextResult.fail(f"OIC API call failed: {str(e)}")

    def _get_auth_headers(self) -> dict:
        return {"Authorization": f"Bearer {self._auth_token}"}

class PostgreSQLIntegrationRepository(IntegrationRepository):
    """PostgreSQL implementation of integration repository."""

    async def save(self, integration: OICIntegration) -> FlextResult[str]:
        """Save integration to PostgreSQL."""
        # Database-specific implementation
        pass
```

### Interface Layer (External Interface)

**Responsibilities:**
- REST API endpoints
- CLI commands
- Web interfaces
- Event handlers

**Dependencies:**
- Application layer
- Framework libraries (FastAPI, Click, etc.)
- HTTP/JSON serialization

```python
# Interface Layer - External interfaces
from fastapi import APIRouter, Depends
from flext_core import FlextResult

router = APIRouter()

class IntegrationAPI:
    """REST API for integration management."""

    def __init__(self, command_handler: ExecuteIntegrationCommand):
        self._command_handler = command_handler

    @router.post("/integrations/{integration_id}/execute")
    async def execute_integration(
        self,
        integration_id: str,
        request: ExecuteIntegrationRequest
    ) -> dict:
        """Execute integration via REST API."""

        command = ExecuteIntegrationCommand(
            integration_id=integration_id,
            pattern_name=request.pattern_name,
            message=request.message,
            context=request.context
        )

        result = await self._command_handler.handle(command)

        if result.is_failure:
            return {"error": result.error, "status": "failed"}

        return {
            "result": result.unwrap().to_dict(),
            "status": "success"
        }
```

## Design Patterns

### Enterprise Integration Patterns

#### **Message Router Pattern**

```python
class MessageRouter:
    """Content-based message routing pattern."""

    def __init__(self, rules: List[RoutingRule]):
        self._rules = rules

    async def route_message(
        self,
        message: dict,
        context: IntegrationContext
    ) -> FlextResult[RoutingResult]:
        """Route message based on content and business rules."""

        # Find matching routing rule
        matching_rule = self._find_matching_rule(message)
        if not matching_rule:
            return FlextResult.fail("No routing rule matches message")

        # Execute routing
        routing_result = await self._execute_routing(
            message,
            matching_rule,
            context
        )

        return routing_result

    def _find_matching_rule(self, message: dict) -> Optional[RoutingRule]:
        """Find routing rule that matches message content."""
        for rule in self._rules:
            if rule.condition.evaluate(message):
                return rule
        return None

    async def _execute_routing(
        self,
        message: dict,
        rule: RoutingRule,
        context: IntegrationContext
    ) -> FlextResult[RoutingResult]:
        """Execute message routing to target endpoint."""
        # Implementation delegates to Oracle OIC adapters
        pass
```

#### **Scatter-Gather Pattern**

```python
class ScatterGatherPattern:
    """Parallel processing with response aggregation."""

    def __init__(self, aggregation_strategy: AggregationStrategy):
        self._aggregation_strategy = aggregation_strategy

    async def execute(
        self,
        request: dict,
        endpoints: List[str],
        context: IntegrationContext
    ) -> FlextResult[AggregatedResponse]:
        """Execute scatter-gather pattern with asyncio concurrency."""

        # Scatter: Send requests to all endpoints concurrently
        tasks = [
            self._send_to_endpoint(request, endpoint, context)
            for endpoint in endpoints
        ]

        # Gather: Wait for all responses (with timeout)
        responses = await asyncio.gather(*tasks, return_exceptions=True)

        # Handle partial failures
        successful_responses = []
        failed_responses = []

        for i, response in enumerate(responses):
            if isinstance(response, Exception):
                failed_responses.append({
                    "endpoint": endpoints[i],
                    "error": str(response)
                })
            else:
                successful_responses.append(response)

        # Aggregate successful responses
        if not successful_responses:
            return FlextResult.fail("All endpoints failed")

        aggregated = self._aggregation_strategy.aggregate(successful_responses)

        return FlextResult.ok(AggregatedResponse(
            aggregated_data=aggregated,
            successful_count=len(successful_responses),
            failed_count=len(failed_responses),
            failures=failed_responses
        ))

    async def _send_to_endpoint(
        self,
        request: dict,
        endpoint: str,
        context: IntegrationContext
    ) -> dict:
        """Send request to individual endpoint."""
        # Implementation uses Oracle OIC adapters
        pass
```

#### **Process Manager Pattern**

```python
class ProcessManager:
    """Long-running business process orchestration."""

    def __init__(
        self,
        process_repo: ProcessRepository,
        message_broker: MessageBroker
    ):
        self._process_repo = process_repo
        self._message_broker = message_broker

    async def start_process(
        self,
        process_definition: ProcessDefinition,
        input_data: dict
    ) -> FlextResult[ProcessInstance]:
        """Start new business process instance."""

        # Create process instance
        process_instance = ProcessInstance(
            process_id=generate_process_id(),
            definition=process_definition,
            state=ProcessState.STARTED,
            data=input_data
        )

        # Persist process state
        save_result = await self._process_repo.save(process_instance)
        if save_result.is_failure:
            return FlextResult.fail(f"Failed to save process: {save_result.error}")

        # Start first step
        first_step_result = await self._execute_next_step(process_instance)

        return first_step_result

    async def handle_step_completion(
        self,
        process_id: str,
        step_result: StepResult
    ) -> FlextResult[ProcessInstance]:
        """Handle completion of process step."""

        # Load current process state
        process_result = await self._process_repo.find_by_id(process_id)
        if process_result.is_failure:
            return FlextResult.fail(f"Process not found: {process_id}")

        process_instance = process_result.unwrap()

        # Update process data with step results
        process_instance.merge_step_result(step_result)

        # Determine next step
        next_step = process_instance.get_next_step()

        if next_step:
            # Continue process
            return await self._execute_next_step(process_instance)
        else:
            # Process completed
            process_instance.state = ProcessState.COMPLETED
            await self._process_repo.save(process_instance)
            return FlextResult.ok(process_instance)

    async def _execute_next_step(
        self,
        process_instance: ProcessInstance
    ) -> FlextResult[ProcessInstance]:
        """Execute next step in process."""
        current_step = process_instance.get_current_step()

        # Send message to execute step
        message_result = await self._message_broker.send_message(
            topic=current_step.topic,
            message={
                "process_id": process_instance.process_id,
                "step_name": current_step.name,
                "data": process_instance.data
            }
        )

        if message_result.is_failure:
            process_instance.state = ProcessState.FAILED
            await self._process_repo.save(process_instance)
            return FlextResult.fail(f"Step execution failed: {message_result.error}")

        process_instance.state = ProcessState.EXECUTING
        await self._process_repo.save(process_instance)

        return FlextResult.ok(process_instance)
```

## Architecture Decision Records

### ADR-001: Clean Architecture Implementation

**Decision**: Implement Clean Architecture with strict layer separation

**Context**: Need maintainable, testable architecture for Oracle OIC integration

**Consequences**:
- ✅ Clear separation of concerns
- ✅ Testable business logic
- ✅ Framework independence
- ⚠️ More complex initial setup
- ⚠️ Learning curve for team

### ADR-002: Domain-Driven Design Tactical Patterns

**Decision**: Use DDD entities, value objects, and domain services

**Context**: Complex Oracle OIC integration domain with rich business logic

**Consequences**:
- ✅ Expressive domain model
- ✅ Ubiquitous language
- ✅ Business logic centralization
- ⚠️ Requires domain expertise
- ⚠️ More classes to maintain

### ADR-003: Railway-Oriented Programming

**Decision**: Use FlextResult for all operations instead of exceptions

**Context**: Need safe error handling in async integration workflows

**Consequences**:
- ✅ Explicit error handling
- ✅ Composable operations
- ✅ No hidden exceptions
- ⚠️ Different from traditional Python
- ⚠️ Requires FlextResult understanding

### ADR-004: FLEXT Ecosystem Integration

**Decision**: Use FLEXT ecosystem exclusively, no custom implementations

**Context**: Need consistency across FLEXT projects and avoid duplication

**Consequences**:
- ✅ Consistent patterns
- ✅ Reduced maintenance
- ✅ Ecosystem benefits
- ⚠️ Dependency on FLEXT libraries
- ⚠️ Less flexibility for custom solutions

### ADR-005: Asyncio-Native Architecture

**Decision**: Build asyncio-first for all Oracle OIC operations

**Context**: Need high performance for enterprise integration scenarios

**Consequences**:
- ✅ High concurrency
- ✅ Efficient I/O handling
- ✅ Modern Python patterns
- ⚠️ Complexity in error handling
- ⚠️ Async/await throughout codebase

---

This architecture guide provides the foundation for building a production-ready Oracle OIC integration library using Clean Architecture and Domain-Driven Design principles within the FLEXT ecosystem.