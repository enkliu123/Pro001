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
                                 <h>this is a pipeline email infomation </h>
                          </html>''',
                          subject: 'pipeline email notify',
                          to: '7572554@qq.com'
         }
    }
}