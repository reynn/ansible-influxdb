node('python') {
  stage('checkout') {
    checkout scm 
  }
  stage('Setup') {
    sh 'pip install -r requirements.test'
  }
  stage('Run Tests') {
    sh 'molecule test'
  }
}
