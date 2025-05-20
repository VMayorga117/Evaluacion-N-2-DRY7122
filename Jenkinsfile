pipeline { 
  agent any
  stages {
    stage('Build') { 
      steps {
        sh 'docker build -t sample-app .'
      }
    }
    stage('run') {
      steps{
        sh 'dockerrun -d -p 9999:9999 --name sample-app sample-app'
      }
    }
  }
}
