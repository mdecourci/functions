import json
import os
import traceback

import azure.functions as func

app = func.FunctionApp()

@app.route(route="hello", methods=["POST"])
def hello_world(req: func.HttpRequest) -> func.HttpResponse:

    try:
        name = req.get_json().get("name", "Hello World!")

        return func.HttpResponse(
            json.dumps({"message": f"Hello, {name}!"}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        error_details = traceback.format_exc()

        return func.HttpResponse(
            body=(
                f"FAILED\n\n"
                f"Error: {str(e)}\n\n"
                f"Stack trace:\n{error_details}"
            ),
            status_code=200
        )


