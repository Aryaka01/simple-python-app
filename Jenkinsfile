pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.9'
        VENV_NAME = 'jenkins_venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
                sh 'ls -la'
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 --version
                    python3 -m pip --version
                    python3 -m venv ${VENV_NAME}
                    . ${VENV_NAME}/bin/activate
                    pip install --upgrade pip setuptools wheel
                    pip install -r requirements-dev.txt
                    pip install -e .
                '''
            }
        }
        
        stage('Code Quality - Lint') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    flake8 src tests --format=junit-xml --output-file=flake8-report.xml || true
                    flake8 src tests
                '''
            }
            post {
                always {
                    // Archive lint results if available
                    archiveArtifacts artifacts: 'flake8-report.xml', allowEmptyArchive: true
                }
            }
        }
        
        stage('Code Quality - Format Check') {
            steps {
                echo 'Checking code formatting...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    black --check --diff src tests
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    pytest --junitxml=pytest-report.xml --cov=myapp --cov-report=xml --cov-report=html --cov-report=term-missing
                '''
            }
            post {
                always {
                    // Publish test results
                    junit 'pytest-report.xml'
                    
                    // Publish coverage reports
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                    
                    // Archive coverage XML for other tools
                    archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
                }
            }
        }
        
        stage('Integration Test') {
            steps {
                echo 'Running integration tests...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    
                    # Test CLI commands
                    echo "Testing CLI calculator..."
                    python -m myapp.cli calc add 5 3
                    python -m myapp.cli calc multiply 4 7
                    
                    echo "Testing CLI greetings..."
                    python -m myapp.cli greet --name "Jenkins"
                    python -m myapp.cli greet --name "Pipeline" --time
                    
                    # Test main application
                    echo "Testing main application..."
                    python -m myapp.app
                    
                    echo "All integration tests passed!"
                '''
            }
        }
        
        stage('Package') {
            steps {
                echo 'Building distribution packages...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    python setup.py sdist bdist_wheel
                    ls -la dist/
                '''
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                echo 'Archiving build artifacts...'
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
                archiveArtifacts artifacts: 'pytest-report.xml', fingerprint: true
                archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed.'
            
            // Clean up virtual environment
            sh '''
                if [ -d "${VENV_NAME}" ]; then
                    rm -rf ${VENV_NAME}
                    echo "Cleaned up virtual environment"
                fi
            '''
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
        unstable {
            echo 'Pipeline is unstable - tests may have failed.'
        }
    }
}
