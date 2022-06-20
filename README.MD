# DevOps - Project
## Infrastructure Code

### MAIN REPO
This is the main repository. In here [`uni_devops_showcase`] are the infrastructure files, seperated from the application code.
The application code is out-sourced into an other repository, namely [`uni_devops_flask_application`].

#### How to clone?
Due to the fact that we have submodules in here, we need to clone recursively.
`git clone --recurse-submodules https://github.com/N10100010/uni_devops_showcase.git`
This will clone this, and the submodule `uni_devops_flask_application`

#### How to run?
Go into the TestApp folder and run
`docker-compose up`

This will start the server.

#### How to access?
Browser: Enter http://0.0.0.0:10000/