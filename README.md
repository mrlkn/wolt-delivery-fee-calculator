# Wolt delivery fee calculator

Made with [FastAPI](https://fastapi.tiangolo.com/), [Pydantic](https://pydantic-docs.helpmanual.io/) and fully dockerized. 

## How to run
```
docker-compose up --build
```
*Keep in mind that I didn't add any env variables and currently in build/Dockerfile uvicorn is set to use `0.0.0.0` 
 as host and `8080` as port.*
 
*If you want to change go ahead to build/dockerfile and change it as you wish, do not forget to expose port in 
docker-compose.yaml*
 
To attach the container
 ```
 docker exec -it $container_id bash
 ```
 
## API Docs
Application has [Swagger](https://swagger.io/) documentation, auto generated with FastAPI and Pydantic. 

After running the application, it is accessible through `http://0.0.0.0:8080/docs` 

You can see the models, endpoints, responses and test it as you wish from the documents.

## Flake8
Application is flake8 compliant. I use [wemake-python-styleguide](https://wemake-python-stylegui.de/en/latest/) and violations can be found [here](https://wemake-python-stylegui.de/en/latest/pages/usage/violations/index.html) 
they are customized and settings can be found in `app/.flake8`

After attaching to the docker container you can check it with `flake8 .`

## Mypy
Application is also [mypy](http://mypy-lang.org/) compliant. After attaching to the docker container you can check it with `mypy .` and settings can be found in `app/mypy .`

## Tests

Added pytest and can be checked with `python -m pytest tests.py`

## Note from dev

As it stated in document for not building production quality code,
I didn't bother to add views etc. Just created the endpoint in the main.py

Apart from it, in order to improve maintability I added delivery configuration to configure all the parameters in same place that plays role in delivery fee. However, it felt like code became more obscure (especially with bad namings) and I couldn't balance it well. So I am not sure if that was the best practice so any feedback is appreciated at this point.
