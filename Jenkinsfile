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
                bat 'dir'
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat '''
                    python --version
                    python -m pip --version
                    python -m venv %VENV_NAME%
                    %VENV_NAME%\\Scripts\\activate.bat && pip install --upgrade pip setuptools wheel
                    %VENV_NAME%\\Scripts\\activate.bat && pip install -r requirements-dev.txt
                    %VENV_NAME%\\Scripts\\activate.bat && pip install -e .
                '''
            }
        }
        
        stage('Code Quality - Lint') {
            steps {
                echo 'Running code quality checks...'
                bat '''
                    %VENV_NAME%\\Scripts\\activate.bat && flake8 src tests --format=junit-xml --output-file=flake8-report.xml || echo "Linting completed with issues"
                    %VENV_NAME%\\Scripts\\activate.bat && flake8 src tests
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'flake8-report.xml', allowEmptyArchive: true
                }
            }
        }
        
        stage('Code Quality - Format Check') {
            steps {
                echo 'Checking code formatting...'
                bat '''
                    %VENV_NAME%\\Scripts\\activate.bat && black --check --diff src tests
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    %VENV_NAME%\\Scripts\\activate.bat && pytest --junitxml=pytest-report.xml --cov=myapp --cov-report=xml --cov-report=html --cov-report=term-missing
                '''
            }
            post {
                always {
                    junit 'pytest-report.xml'
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                    archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
                }
            }
        }
        
        stage('Integration Test') {
            steps {
                echo 'Running integration tests...'
                bat '''
                    %VENV_NAME%\\Scripts\\activate.bat && python -m myapp.cli calc add 5 3
                    %VENV_NAME%\\Scripts\\activate.bat && python -m myapp.cli calc multiply 4 7
                    %VENV_NAME%\\Scripts\\activate.bat && python -m myapp.cli greet --name "Jenkins"
                    %VENV_NAME%\\Scripts\\activate.bat && python -m myapp.cli greet --name "Pipeline" --time
                    %VENV_NAME%\\Scripts\\activate.bat && python -m myapp.app
                    echo "All integration tests passed!"
                '''
            }
        }
        
        stage('Package') {
            steps {
                echo 'Building distribution packages...'
                bat '''
                    %VENV_NAME%\\Scripts\\activate.bat && python setup.py sdist bdist_wheel
                    dir dist\\
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
            bat '''
                if exist "%VENV_NAME%" (
                    rmdir /s /q "%VENV_NAME%"
                    echo "Cleaned up virtual environment"
                )
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
