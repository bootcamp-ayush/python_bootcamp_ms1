#!groovy

pipeline {
        options {
            buildDiscarder(logRotator(artifactDaysToKeepStr: '30', artifactNumToKeepStr: '5', daysToKeepStr: '30', numToKeepStr: '5'))
        }
        environment{
            PROJECT_NAME = 'python_bootcamp_ms1'
            VERSION = '1.0.0'
            NAMESPACE = 'python_bootcamp'
            DOCKER_REGISTRY_URL = ""
            DOCKER_REGISTRY = ''
            SONAR_TOKEN = credentials('sonarqube')
            RELEASE_NAME = 'python_bootcamp_ms1'
            /* BRANCH =  sh(script: 'echo ${BRANCH_NAME}', , returnStdout: true).trim()*/

        }
        agent none
        stages {
            stage('Install Requirements') {
                agent { docker 'python:3.8.0-alpine3.10' }
                steps {
                       sh '''
                        pip install -r requirements.txt
                        python -m pytest tests/unittests -s --junitxml='pyTests.xml' --alluredir='allure-results'
                        python -m pytest tests/unittests --cov=.  --cov-report xml:coverage-reports/coverage.xml --cov-report html:coverage-reports --cov-report annotate:coverage-reports --cov-report term-missing
                       '''
                    }
                post {
                    always {
                        junit 'pyTests.xml'
                    }
                }
            }

            /*
            stage('Unit tests') {
                steps {
                    sh '''
                    python -m pytest tests/unittests -s --junitxml='pyTests.xml' --alluredir='allure-results'
                    '''
                }
            }

            stage('Coverage') {
                steps {
                    sh '''
                    python -m pytest tests/unittests --cov=.  --cov-report xml:coverage-reports/coverage.xml --cov-report html:coverage-reports --cov-report annotate:coverage-reports --cov-report term-missing
                    '''
                }
            }
            */
            stage('Sonar') {
                agent { docker 'sonarsource/sonar-scanner-cli:4.2' }
                steps {
                    sh '''
                    printenv
                    sonar-scanner -X \
                            -Dsonar.projectKey=bootcamp.python_bootcamp_ms1 \
                            -Dsonar.projectName=python_bootcamp_ms1 \
                            -Dsonar.host.url=https://localhost:9000 \
                            -Dsonar.sources=. \
                            -Dsonar.tests=tests/unittests \
                            -Dsonar.login=${SONAR_TOKEN} \
                            -Dsonar.python.coverage.reportPaths=coverage-reports/coverage.xml \
                            -Dsonar.python.xunit.reportPath=pyTests.xml \
                            -Dsonar.projectVersion=${env.BUILD_TAG}
                    '''
                }
            }
        }
    }
