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
        writeFile(file: '/var/jenkins_home/workspace/test-automation_develop/results/xml/first.xml', text: 'test', encoding: 'utf-8')
        writeFile(file: '/screenshots/*.*', text: 'screen')
      }
    }

  }
}