pipeline{
    agent any
    stages {
        stage("autotest"){
            steps{
                bat 'python main.py'
            }
        }
    }
    post {
        always {
    // One or more steps need to be included within each condition's block.
        emailext body: '''<html>
                                 <h>this is a pipeline info email </h>
                          </html>''',
                          subject: 'job ${JOB_BASE_NAME},result: ${currentBuild.currentResult}',
                          to: '7572554@qq.com'
         }
    }
}