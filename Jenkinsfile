node('python') {
  stage('checkout') {
    checkout scm
  }
  stage('Setup') {
    sh 'sudo apt-get install -y $(cat requirements.apt)'
    sh 'pip install -r requirements.test'
  }
  stage('Run Tests') {
    if (env.BRANCH_NAME != 'master') {
      def path = pwd()
      def folder = path.substring(path.lastIndexOf('/')+1)
      def playbook = """
      ---
      - hosts: all
        roles:
          - role: ${folder}
      """
      sh "echo \"${playbook}\" > playbook.yml"
      sh 'molecule test'
    } else {
      println 'No test run on master branch'
    }
  }
}
