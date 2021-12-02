# Tartiflette automated test failures

This repo exists to demonstrate the difficulty of writing automated
tests with [Tartiflette](https://tartiflette.io). It's possible
to write _one_ test, but subsequent tests fail due to setup/teardown
issues.

This repo is a fairly minimal reproducible test case. The code uses
the latest version of Tartiflette and tartiflette-aiohttp, and the
tests use pytest with some commonly-used plugins. In all cases,
the first test you run will pass, but subsequent tests will fail,
with error messages indicating that Tartiflette is not doing
setup or teardown correctly. Here's an example output:

<details>
<summary>Here's an example of the test failure output</summary>
<pre>
============================= test session starts ==============================
platform linux -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /usr/src/app
plugins: asyncio-0.16.0, aiohttp-0.3.0
collected 3 items

tests/query/test_goodbye.py .                                            [ 33%]
tests/query/test_hello.py EE                                             [100%]

==================================== ERRORS ====================================
________________________ ERROR at setup of test_hello_1 ________________________

self = <tartiflette.directive.directive.Directive object at 0xffffb955c4c0>
schema = GraphQLSchema(name='default')

    def bake(self, schema: "GraphQLSchema") -> None:
        """
        Sets the directive implementation into the schema directive definition.
        :param schema: the GraphQLSchema instance linked to the directive
        :type schema: GraphQLSchema
        """
        if not self._implementation:
            raise MissingImplementation(
                f"No implementation given for directive < {self.name} >"
            )

        try:
>           directive = schema.find_directive(self.name)

/usr/local/lib/python3.10/site-packages/tartiflette/directive/directive.py:61:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = GraphQLSchema(name='default'), name = 'deprecated'

    def find_directive(self, name: str) -> "GraphQLDirective":
        """
        Returns the defined directive corresponding to the name.
        :param name: name of the directive to return
        :type name: str
        :return: the defined directive
        :rtype: GraphQLDirective
        """
>       return self._directive_definitions[name]
E       KeyError: 'deprecated'

/usr/local/lib/python3.10/site-packages/tartiflette/schema/schema.py:363: KeyError

During handling of the above exception, another exception occurred:

args = ()
kwargs = {'aiohttp_client': <function aiohttp_client.<locals>.go at 0xffffb9363400>, 'app': <Application 0xffffb944fdf0>}
loop = <_UnixSelectorEventLoop running=False closed=False debug=False>
setup = <function pytest_fixture_setup.<locals>.wrapper.<locals>.setup at 0xffffb93609d0>

    def wrapper(*args, **kwargs):
        loop = fixture_stripper.get_and_strip_from(
            FixtureStripper.EVENT_LOOP, kwargs
        )

        async def setup():
            res = await coro(*args, **kwargs)
            return res

>       return loop.run_until_complete(setup())

/usr/local/lib/python3.10/site-packages/pytest_asyncio/plugin.py:160:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/usr/local/lib/python3.10/asyncio/base_events.py:641: in run_until_complete
    return future.result()
/usr/local/lib/python3.10/site-packages/pytest_asyncio/plugin.py:157: in setup
    res = await coro(*args, **kwargs)
tests/conftest.py:22: in client
    return await aiohttp_client(TestServer(app))
/usr/local/lib/python3.10/site-packages/aiohttp/pytest_plugin.py:371: in go
    await client.start_server()
/usr/local/lib/python3.10/site-packages/aiohttp/test_utils.py:291: in start_server
    await self._server.start_server(loop=self._loop)
/usr/local/lib/python3.10/site-packages/aiohttp/test_utils.py:125: in start_server
    await self.runner.setup()
/usr/local/lib/python3.10/site-packages/aiohttp/web_runner.py:279: in setup
    self._server = await self._make_server()
/usr/local/lib/python3.10/site-packages/aiohttp/web_runner.py:375: in _make_server
    await self._app.startup()
/usr/local/lib/python3.10/site-packages/aiohttp/web_app.py:417: in startup
    await self.on_startup.send(self)
/usr/local/lib/python3.10/site-packages/aiosignal/__init__.py:36: in send
    await receiver(*args, **kwargs)  # type: ignore
/usr/local/lib/python3.10/site-packages/tartiflette_aiohttp/__init__.py:109: in _cook_on_startup
    await app["ttftt_engine"].cook(
/usr/local/lib/python3.10/site-packages/tartiflette/engine.py:319: in cook
    self._schema = await SchemaBakery.bake(
/usr/local/lib/python3.10/site-packages/tartiflette/schema/bakery.py:63: in bake
    await schema.bake(
/usr/local/lib/python3.10/site-packages/tartiflette/schema/schema.py:1171: in bake
    SchemaRegistry.bake_registered_objects(self)
/usr/local/lib/python3.10/site-packages/tartiflette/schema/registry.py:233: in bake_registered_objects
    obj.bake(schema)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <tartiflette.directive.directive.Directive object at 0xffffb955c4c0>
schema = GraphQLSchema(name='default')

    def bake(self, schema: "GraphQLSchema") -> None:
        """
        Sets the directive implementation into the schema directive definition.
        :param schema: the GraphQLSchema instance linked to the directive
        :type schema: GraphQLSchema
        """
        if not self._implementation:
            raise MissingImplementation(
                f"No implementation given for directive < {self.name} >"
            )

        try:
            directive = schema.find_directive(self.name)
            directive.implementation = self._implementation
            directive.arguments_coercer = (
                self._arguments_coercer or schema.default_arguments_coercer
            )
        except KeyError:
>           raise UnknownDirectiveDefinition(
                f"Unknown Directive Definition {self.name}"
            )
E           tartiflette.types.exceptions.tartiflette.UnknownDirectiveDefinition: Unknown Directive Definition deprecated

/usr/local/lib/python3.10/site-packages/tartiflette/directive/directive.py:67: UnknownDirectiveDefinition
________________________ ERROR at setup of test_hello_2 ________________________

self = <tartiflette.directive.directive.Directive object at 0xffffb955c4c0>
schema = GraphQLSchema(name='default')

    def bake(self, schema: "GraphQLSchema") -> None:
        """
        Sets the directive implementation into the schema directive definition.
        :param schema: the GraphQLSchema instance linked to the directive
        :type schema: GraphQLSchema
        """
        if not self._implementation:
            raise MissingImplementation(
                f"No implementation given for directive < {self.name} >"
            )

        try:
>           directive = schema.find_directive(self.name)

/usr/local/lib/python3.10/site-packages/tartiflette/directive/directive.py:61:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = GraphQLSchema(name='default'), name = 'deprecated'

    def find_directive(self, name: str) -> "GraphQLDirective":
        """
        Returns the defined directive corresponding to the name.
        :param name: name of the directive to return
        :type name: str
        :return: the defined directive
        :rtype: GraphQLDirective
        """
>       return self._directive_definitions[name]
E       KeyError: 'deprecated'

/usr/local/lib/python3.10/site-packages/tartiflette/schema/schema.py:363: KeyError

During handling of the above exception, another exception occurred:

args = ()
kwargs = {'aiohttp_client': <function aiohttp_client.<locals>.go at 0xffffb8e66f80>, 'app': <Application 0xffffb8a73a00>}
loop = <_UnixSelectorEventLoop running=False closed=False debug=False>
setup = <function pytest_fixture_setup.<locals>.wrapper.<locals>.setup at 0xffffb8eb1990>

    def wrapper(*args, **kwargs):
        loop = fixture_stripper.get_and_strip_from(
            FixtureStripper.EVENT_LOOP, kwargs
        )

        async def setup():
            res = await coro(*args, **kwargs)
            return res

>       return loop.run_until_complete(setup())

/usr/local/lib/python3.10/site-packages/pytest_asyncio/plugin.py:160:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/usr/local/lib/python3.10/asyncio/base_events.py:641: in run_until_complete
    return future.result()
/usr/local/lib/python3.10/site-packages/pytest_asyncio/plugin.py:157: in setup
    res = await coro(*args, **kwargs)
tests/conftest.py:22: in client
    return await aiohttp_client(TestServer(app))
/usr/local/lib/python3.10/site-packages/aiohttp/pytest_plugin.py:371: in go
    await client.start_server()
/usr/local/lib/python3.10/site-packages/aiohttp/test_utils.py:291: in start_server
    await self._server.start_server(loop=self._loop)
/usr/local/lib/python3.10/site-packages/aiohttp/test_utils.py:125: in start_server
    await self.runner.setup()
/usr/local/lib/python3.10/site-packages/aiohttp/web_runner.py:279: in setup
    self._server = await self._make_server()
/usr/local/lib/python3.10/site-packages/aiohttp/web_runner.py:375: in _make_server
    await self._app.startup()
/usr/local/lib/python3.10/site-packages/aiohttp/web_app.py:417: in startup
    await self.on_startup.send(self)
/usr/local/lib/python3.10/site-packages/aiosignal/__init__.py:36: in send
    await receiver(*args, **kwargs)  # type: ignore
/usr/local/lib/python3.10/site-packages/tartiflette_aiohttp/__init__.py:109: in _cook_on_startup
    await app["ttftt_engine"].cook(
/usr/local/lib/python3.10/site-packages/tartiflette/engine.py:319: in cook
    self._schema = await SchemaBakery.bake(
/usr/local/lib/python3.10/site-packages/tartiflette/schema/bakery.py:63: in bake
    await schema.bake(
/usr/local/lib/python3.10/site-packages/tartiflette/schema/schema.py:1171: in bake
    SchemaRegistry.bake_registered_objects(self)
/usr/local/lib/python3.10/site-packages/tartiflette/schema/registry.py:233: in bake_registered_objects
    obj.bake(schema)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <tartiflette.directive.directive.Directive object at 0xffffb955c4c0>
schema = GraphQLSchema(name='default')

    def bake(self, schema: "GraphQLSchema") -> None:
        """
        Sets the directive implementation into the schema directive definition.
        :param schema: the GraphQLSchema instance linked to the directive
        :type schema: GraphQLSchema
        """
        if not self._implementation:
            raise MissingImplementation(
                f"No implementation given for directive < {self.name} >"
            )

        try:
            directive = schema.find_directive(self.name)
            directive.implementation = self._implementation
            directive.arguments_coercer = (
                self._arguments_coercer or schema.default_arguments_coercer
            )
        except KeyError:
>           raise UnknownDirectiveDefinition(
                f"Unknown Directive Definition {self.name}"
            )
E           tartiflette.types.exceptions.tartiflette.UnknownDirectiveDefinition: Unknown Directive Definition deprecated

/usr/local/lib/python3.10/site-packages/tartiflette/directive/directive.py:67: UnknownDirectiveDefinition
=========================== short test summary info ============================
ERROR tests/query/test_hello.py::test_hello_1 - tartiflette.types.exceptions....
ERROR tests/query/test_hello.py::test_hello_2 - tartiflette.types.exceptions....
========================= 1 passed, 2 errors in 0.17s ==========================
</pre>
</details>

## Docker

To aid in reproductibility, I've also include a `Dockerfile`
in this repo. Here's how to use it:

```
docker build -t tartiflette_failure .
docker run -it tartiflette_failure
```