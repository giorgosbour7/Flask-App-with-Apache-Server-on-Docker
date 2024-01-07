This is the repo for running a python app on apache in a docker container

Many of the docker repo's out there use flask local server in their images. This repo is for a more production ready environment.

I have structured my application to run each service in a separate Docker file. This approach aims to avoid confusion, as both services are treated independently.

This way, changes and metrics for each service are isolated and managed effectively.
