from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from _shared.domain.entities.bases.entity_base import Base

# Todas las entidades
from _shared.domain.entities.access_key import AccessKey
from _shared.domain.entities.account_account_group import AccountAccountGroup
from _shared.domain.entities.account_group import AccountGroup
from _shared.domain.entities.alert import Alert
from _shared.domain.entities.asset_name import AssetName
from _shared.domain.entities.asset_type import AssetType
from _shared.domain.entities.cloud_accounts import CloudAccounts
from _shared.domain.entities.compliance_standard import ComplianceStandard
from _shared.domain.entities.control import Control
from _shared.domain.entities.control_section import ControlSection
from _shared.domain.entities.csp import CSP
from _shared.domain.entities.event import Event
from _shared.domain.entities.event_alert import EventAlert
from _shared.domain.entities.permission_group import PermissionGroup
from _shared.domain.entities.policy import Policy
from _shared.domain.entities.policy_csp import PolicyCSP
from _shared.domain.entities.role import Role
from _shared.domain.entities.role_account_group import RoleAccountsGroup
from _shared.domain.entities.role_group import RoleGroup
from _shared.domain.entities.role_users import RoleUsers
from _shared.domain.entities.section_policy import SectionPolicy
from _shared.domain.entities.service_name import ServiceName
from _shared.domain.entities.tenant_info import TenantInfo
from _shared.domain.entities.user import User
from _shared.domain.db.base_repository import BaseRepository


class ApiDbContext:
    def __init__(self, connection_string: str):
        # Crear engine async
        self.engine = create_async_engine(
            connection_string,
            echo=False,
            future=True
        )

        # Crear async_sessionmaker
        self.AsyncSessionLocal = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False
        )

        # Repositorios como lambdas
        self._repos = {
            "access_keys": lambda db: BaseRepository(AccessKey, db),
            "account_account_groups": lambda db: BaseRepository(AccountAccountGroup, db),
            "account_groups": lambda db: BaseRepository(AccountGroup, db),
            "alerts": lambda db: BaseRepository(Alert, db),
            "asset_names": lambda db: BaseRepository(AssetName, db),
            "asset_types": lambda db: BaseRepository(AssetType, db),
            "cloud_accounts": lambda db: BaseRepository(CloudAccounts, db),
            "compliance_standards": lambda db: BaseRepository(ComplianceStandard, db),
            "controls": lambda db: BaseRepository(Control, db),
            "control_sections": lambda db: BaseRepository(ControlSection, db),
            "csps": lambda db: BaseRepository(CSP, db),
            "events": lambda db: BaseRepository(Event, db),
            "event_alerts": lambda db: BaseRepository(EventAlert, db),
            "permission_groups": lambda db: BaseRepository(PermissionGroup, db),
            "policies": lambda db: BaseRepository(Policy, db),
            "policy_csps": lambda db: BaseRepository(PolicyCSP, db),
            "roles": lambda db: BaseRepository(Role, db),
            "role_account_groups": lambda db: BaseRepository(RoleAccountsGroup, db),
            "role_groups": lambda db: BaseRepository(RoleGroup, db),
            "role_users": lambda db: BaseRepository(RoleUsers, db),
            "section_policies": lambda db: BaseRepository(SectionPolicy, db),
            "service_names": lambda db: BaseRepository(ServiceName, db),
            "tenants": lambda db: BaseRepository(TenantInfo, db),
            "users": lambda db: BaseRepository(User, db),
        }

    async def create_tables(self):
        # Crear todas las tablas de forma async
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        # Generador de sesiones async para FastAPI
        async with self.AsyncSessionLocal() as session:
            yield session

    # Métodos para obtener repositorios con sesión async
    async def access_keys(self, db: AsyncSession):
        return self._repos["access_keys"](db)

    async def account_account_groups(self, db: AsyncSession):
        return self._repos["account_account_groups"](db)

    async def account_groups(self, db: AsyncSession):
        return self._repos["account_groups"](db)

    async def alerts(self, db: AsyncSession):
        return self._repos["alerts"](db)

    async def asset_names(self, db: AsyncSession):
        return self._repos["asset_names"](db)

    async def asset_types(self, db: AsyncSession):
        return self._repos["asset_types"](db)

    async def cloud_accounts(self, db: AsyncSession):
        return self._repos["cloud_accounts"](db)

    async def compliance_standards(self, db: AsyncSession):
        return self._repos["compliance_standards"](db)

    async def controls(self, db: AsyncSession):
        return self._repos["controls"](db)

    async def control_sections(self, db: AsyncSession):
        return self._repos["control_sections"](db)

    async def csps(self, db: AsyncSession):
        return self._repos["csps"](db)

    async def events(self, db: AsyncSession):
        return self._repos["events"](db)

    async def event_alerts(self, db: AsyncSession):
        return self._repos["event_alerts"](db)

    async def permission_groups(self, db: AsyncSession):
        return self._repos["permission_groups"](db)

    async def policies(self, db: AsyncSession):
        return self._repos["policies"](db)

    async def policy_csps(self, db: AsyncSession):
        return self._repos["policy_csps"](db)

    async def roles(self, db: AsyncSession):
        return self._repos["roles"](db)

    async def role_account_groups(self, db: AsyncSession):
        return self._repos["role_account_groups"](db)

    async def role_groups(self, db: AsyncSession):
        return self._repos["role_groups"](db)

    async def role_users(self, db: AsyncSession):
        return self._repos["role_users"](db)

    async def section_policies(self, db: AsyncSession):
        return self._repos["section_policies"](db)

    async def service_names(self, db: AsyncSession):
        return self._repos["service_names"](db)

    async def tenants(self, db: AsyncSession):
        return self._repos["tenants"](db)

    async def users(self, db: AsyncSession):
        return self._repos["users"](db)
