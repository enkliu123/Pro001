pipeline{
    agent any
    environment{
        JobName = "自动化集成测试项目"
    }
    parameters{
        string(name: 'Name',defaultValue: 'Helen', description: 'beautiful girl!')
    }
    stages {
        stage("autotest"){
            steps{
                bat 'python main.py'
            }
        }
        stage("Custom Parameters"){
            steps{
                echo "${parameters.Name} ,My beautiful daughter!"
            }
        }
    }
    post {
        always {
    // One or more steps need to be included within each condition's block.
        emailext body: '''<html>
                                 <h>this is a pipeline info email </h>
                          </html>''',
                          subject: "Project ${env.JobName},job ${env.JOB_BASE_NAME},result: ${currentBuild.currentResult}",
                          to: '7572554@qq.com'
         }
    }
}