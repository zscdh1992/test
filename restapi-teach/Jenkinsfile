pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'build.bat %BUILD_NUMBER%'

            }
        }

        stage('Dev_Test'){
            steps {
                input '等待开发人员测试通过，通过后再继续'
            }
        }

        stage('QA_Test') {
            steps {
                echo '执行自动化部署...'
                bat 'python d:/autodeploy.py'
                echo '执行自动化测试...'

                dir ('d:\\projects\\sonqqin\\restapi-autotest') {
                    bat 'robot --pythonpath . --name build_%BUILD_NUMBER% -L debug tc'
                }

            }
        }
    }
}