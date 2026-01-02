r'''
# File and folder structure for development
During development, files like app.py, tests.py or other python files might be used to call and test the module under development.
These files are only relevant during development.

Development is done in the "DEV" branch.

The module I want to develope is located in a sub folder like "My Module A".

<img src="./My Development Guide-Prozess - DEV.png">

## git commands
``` shell
# Create / clone the local repository
git clone "https://github.com/…"
# Create the DEV branch
git checkout -b "DEV"

#------------------------------
# Add and commit development steps
git add …
git commit -m "..."

#------------------------------
# When pushing the DEV branch the first time, set the upstream
git push –set-upstream origin DEV

# Push the commits
git push
```

# Version branches
Versions I want to provide will be brought out as a `git subtree` version branch.
So all the files needed for development can be hidden and the relevant part can be used elsewhere.

The docs also will be brougth out as a `git subtree` branch.

<img src="./My Development Guide-Prozess - Version 1.0.png">

## git commands
``` shell
# Split the version of the module into its version branch
git subtree split -P "My Modul A" -b v1.0

# To push the version branch, set the upstream
git push –set-upstream origin v1.0

# Split the version of the modules documentation into its version branch and push it
git subtree split -P "docs" -b v1.0_doc
git push –set-upstream origin v1.0_doc

# Push the commits
git push
```

# The overall development process
The overall development process is based on the structure described above.

To start or continue development, I check out the "DEV" branch. To provide a new version, I create a `git subtree` for that version.

<img src="./My Development Guide-Prozess - Development Process.png">

# Integration of other modules
Versions of different modules can be integrated as `git submodule`.

<img src="./My Development Guide-Prozess - Integration of Modules.png">

## git commands
``` shell
# Create / clone the local repository
git clone „https://github.com/…“
# Create the DEV branch
git checkout -b „DEV“

#------------------------------
# Add and commit development steps
git add …
git commit -m „…“

#------------------------------
# When pushing the DEV branch the first time, set the upstream
git push –set-upstream origin DEV

# Push the commits
git push

#------------------------------
# Integrate a Module from an other repository as submodule
git submodule add „https://github.com/…“ „Modul A“

# Initialise the submodule within the local configuration
git submodule init 
# Retrieve the data from the submodule
git submodule update

# Chose a specific version of the submodule
git config -f .gitmodules „submodule.Modul A.branch“ v1.0

#------------------------------
# Add, commit and push the integration of the submodule
git add ...
git commit ...
git push

#------------------------------
# Update all submodules
git submodule update --remote
```

'''
