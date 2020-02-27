pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Run tests') {
      steps {
        sh 'pytest -s tests --junitxml=results/xml/first.xml'
      }
    }

  }
}