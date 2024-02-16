import subprocess
from typing import Any, Union

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool


class LinearCliTool(BuiltinTool):
    def _invoke(self,
                user_id: str,
               tool_parameters: dict[str, Any],
        ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        command = tool_parameters.get('command', '')
        if not command:
            return self.create_text_message('Please input command')
        # data = data.split(';')
        print(command)

        # p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # # for line in p.stdout.readlines():
        #     # print(line)
        # retval = p.wait()
        # print('retval is ' + str(retval))

        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
        retval = result.stdout
        error = result.stderr

        if error:
            return self.create_text_message([self.create_text_message(error)])

        return [
            # self.create_text_message('the linear cli is running'),
            self.create_text_message('the sync cli ret is:\r\n' + str(retval)),
            # self.create_blob_message(blob=buf.read(),
            #                         meta={'mime_type': 'image/png'})
        ]
