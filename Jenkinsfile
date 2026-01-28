pipeline {
    agent any

    environment {
        // Your GitHub credentials stored in Jenkins
        GITHUB_CREDS = credentials('github-PAT')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install sphinx and sphinx-needs
                //sh 'cd AWS_Terraform'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Build HTML') {
            steps {
                // Build the documentation into the 'build' folder
                sh 'sphinx-build -b html docs/ build/html'
            }
        }

        stage('Deploy to GitHub Pages') {
            steps {
                script {
                    sh """
                        cd build/html
                        git init
                        git add .
                        git commit -m "Deploy docs version ${env.BUILD_NUMBER}"
                        # Push to the 'gh-pages' branch of your repo
                        git push -f git@github.com:gokulraman/AWS_Terraform.git main:gh-pages
                    """
                }
            }
        }
    }
}