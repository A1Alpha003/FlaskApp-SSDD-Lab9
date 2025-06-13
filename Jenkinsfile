pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Add commands for building the application, e.g., mvn clean install for a Maven project
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add commands for running tests, e.g., npm test for a Node.js project
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add commands for deployment, e.g., copying files to a server
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
