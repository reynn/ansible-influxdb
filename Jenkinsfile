node('python') {
  stage('checkout') {
    scm checkout
  }
  stage('Setup') {
    sh 'pip install -r requirements.test'
  }
  stage('Run Tests') {
    sh 'molecule test'
  }
}
