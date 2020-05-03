pipeline {
   agent { dockerfile true }

   stages {
      stage('Tests') {
         steps {
            bash 'pytest'
            step([$class: 'XUnitBuilder', thresholds: [[$class: 'FailedThreshold', unstableThreshold: '1']], tools: [[$class: 'XUnitDotNetTestType', pattern: '*results_xunit.xml']]])
         }
      }
   }
}