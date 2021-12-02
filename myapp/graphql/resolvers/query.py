from typing import TypedDict

from tartiflette import Resolver
from tartiflette.execution.types import ResolveInfo


class Args(TypedDict):
    name: str


@Resolver("Query.hello")
async def resolve_hello(
    parent: None, args: Args, ctx: dict, info: ResolveInfo
) -> str:
    return f"Hello {args['name']}"

@Resolver("Query.goodbye")
async def resolve_goodbye(
    parent: None, args: Args, ctx: dict, info: ResolveInfo
) -> str:
    return f"Goodbye {args['name']}"