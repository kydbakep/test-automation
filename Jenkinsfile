pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Run tests') {
      steps {
        sh 'pytest -s tests --junitxml=test-results/xml/result.xml'
      }
    }
  }
}
