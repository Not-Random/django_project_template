## INTRODUCTION



That will start the PostgreSQL container and the App container. I also included 
a service for NGINX web server if you want to deploy this project to production.
 Take a look at the docker/docker-compose.yml file and uncomment the Nginx 
 section at the bottom.

## HOW TO USE / INITIAL SETUP
- Dependencies:
    - Make sure there is an environment variables text file called '.env' 
    (without the quotes, of course) and save it the BASE_DIR, which is where
    the 'manage.py' file is. This file should include the following:

    ```
        # pick the environment you want to deploy: prod/dev/local/local_wo_container
        #       Production = prod
        #       Development = dev
        #       Local (with container) = local
        #       Local (without container) = local_wo_container
        # if no environment is indicated, the default is 'local_wo_container'

        SELECTED_ENV="local_wo_container"
    ```

    indicate in the 'SELECTED_ENV' value what is the environment you want to 
    use. For beginners, the leave the selection as "local_wo_container", which 
    means you will run the project locally, without docker in your computer, 
    using the included Sqlite3 database.

    This '.env' file defines what will be the settings to be used for Database, 
    whether to use Docker or not, etc, and that will define how Django will 
    behave, by ingesting different variables that will be provided in the 
    different .env files that will be needed for the different scenarios 
    (development, production, etc.)

```
     ++++++++++++++++++++++++++++++++++++++++++++++
        IMPORTANT: make sure to add a line 'environments/' (without quotes) to 
        your .gitignore file or you will publish all of your secrets to wherever
         repository you are uploading your code to (e.g. GitHub, 
         Azure DevOps, etc.)!!!
    ++++++++++++++++++++++++++++++++++++++++++++++
``` 
    - To run the project, execute the following command:

    ```
        $ python manage.py runserver
    ```
    and you should see something like this:

    ```
        Django version 3.1.4, using settings 'project.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.
    ```