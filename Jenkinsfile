pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create venv & Install Deps') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    ${VENV}/bin/python -m pip install --upgrade pip
                    ${VENV}/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Build HTML') {
            steps {
                sh '''
                    ${VENV}/bin/sphinx-build -b html docs/ build/html
                '''
            }
        }

        stage('Deploy to GitHub Pages') {
            steps {
                sh '''
                    cd build/html
                    git init -b main
                    git add .
                    git commit -m "Deploy docs build ${BUILD_NUMBER}"
                    git push -f https://${GITHUB_CREDS}@github.com/gokulraman/AWS_Terraform.git HEAD:gh-pages

                '''
            }
        }
    }
}
//                    git push -f git@github.com:gokulraman/AWS_Terraform.git HEAD:gh-pages