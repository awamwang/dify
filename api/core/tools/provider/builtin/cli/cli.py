from core.tools.errors import ToolProviderCredentialValidationError
from core.tools.provider.builtin.cli.tools.sync import LinearCliTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController


class CliProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict) -> None:
        try:
            LinearCliTool().fork_tool_runtime(
                meta={
                    "credentials": credentials,
                }
            ).invoke(
                user_id='',
                tool_parameters={
                    "command": "ls -l",
                },
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))