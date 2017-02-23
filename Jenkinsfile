node('python') {
  stage('checkout') {
    checkout scm
  }
  stage('Setup') {
    sh 'sudo apt install -y $(cat requirements.apt)'
    sh 'pip install -r requirements.test'
  }
  stage('Run Tests') {
    sh 'molecule test'
  }
}
