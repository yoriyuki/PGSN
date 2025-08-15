import sys

sys.path.append("..")
import pprint
from pgsn.gsn_term import *

solarwinds = goal(description="Binary Repositoryが安全である",
                  support=strategy(description="Pushが安全であるためには?",
                                   #Root tree(Artifact)
                              sub_goal1=[goal(description="Artifact Consumes Push が安全である",
                                               support=goal(description="各ArtifactによるConsumesが安全である",
                                                    support=strategy(description="artifactについて分解",
                                                         #Validation Data Query tree
                                                           sub_goal2=[goal(description="Validation Build Reportが安全である",
                                                           support=strategy(description="Vulunarbility data Queryが安全であるためには?",
                                                                            #Carries Out Vulnarability Data Query Tree
                                                                sub_goal3=[goal(description="Carries Out Vulunarbility data Queryが安全",
                                                                               support=strategy(description="resourceについて分解",
                                                                                               sub_goal4=[goal(description="Tektlon Security CI/CD pipeline が安全",
                                                                                                               support=strategy("Uses Tektlon Security CI/CD pipeline が安全であるためには？",
                                                                                                                              sub_goal5=[goal(description="Uses Resourceが安全",
                                                                                                                                              support=strategy("CI/CD Controller Usesが安全であるためには？",
                                                                                                                                                              sub_goal5=[goal(description="P1",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="P2",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="P3",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="P4",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="P5",
                                                                                                                                                                               support=evidence(description = "none"))]
                                                                                                                                                              )
                                                                                                                                            ),
                                                                                                                                        goal(description="S1",
                                                                                                                                             support=evidence(description = "none")),
                                                                                                                                        goal(description="S2",
                                                                                                                                             support=evidence(description = "none")),
                                                                                                                                        goal(description="S3",
                                                                                                                                             support=evidence(description = "none"))]
                                                                                                                                     )
                                                                                                              ),
                                                                                                          goal(description="Jfrog Xray が安全",
                                                                                                               support=strategy("Uses Jfrog Xray が安全であるためには？",
                                                                                                                                sub_goal6=[goal(description="R1",
                                                                                                                                             support=evidence(description = "none")),
                                                                                                                                        goal(description="R2",
                                                                                                                                             support=evidence(description = "none")),
                                                                                                                                        goal(description="R3",
                                                                                                                                             support=evidence(description = "none"))]
                                                                                                                                )
                                                                                                              )]
                                                                                               )
                                                                               ),
                                                                                #Consumes Vulunarability Data Query tree
                                                                                goal(description="Consumes Vulunarbility data Queryが安全",
                                                                                     support=strategy("Sourcecode Consumes が安全であるためには？",
                                                                                                goal(description="Produce Sourcecodeが安全",
                                                                                                      support=strategy("Fetch Produce が安全であるためには？",
                                                                                                                       sub_goals7=[goal(description="Consumes Fetchが安全",
                                                                                                                                              support=strategy("Repository Consumesが安全であるためには？",
                                                                                                                                                              sub_goal8=[goal(description="A1",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="A2",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="A3",
                                                                                                                                                                               support=evidence(description = "none"))]
                                                                                                                                                              )
                                                                                                                                       ),
                                                                                                                                        goal(description="Carries Out Fetchが安全",
                                                                                                                                              support=strategy("GitHub Carries Outが安全であるためには？",
                                                                                                                                                              sub_goal9=[goal(description="Uses Resourceが安全",
                                                                                                                                                                              support=strategy("Ballistaが安全であるためには？",
                                                                                                                                                                                                sub_goal10=[goal(description="P1",
                                                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                                                          goal(description="P2",
                                                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                                                          goal(description="P3",
                                                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                                                          goal(description="P4",
                                                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                                                          goal(description="P5",
                                                                                                                                                                                                               support=evidence(description = "none"))]
                                                                                                                                                                                              )
                                                                                                                                                                             ),
                                                                                                                                                                          goal(description="R1",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="R2",
                                                                                                                                                                               support=evidence(description = "none")),
                                                                                                                                                                          goal(description="R3",
                                                                                                                                                                               support=evidence(description = "none"))]
                                                                                                                                                              )
                                                                                                                                            ),
                                                                                                                                       goal(description="A1",
                                                                                                                                             support=evidence(description = "none")),
                                                                                                                                        goal(description="A2",
                                                                                                                                             support=evidence(description = "none")),
                                                                                                                                        goal(description="A3",
                                                                                                                                             support=evidence(description = "none"))]
                                                                                                                      )
                                                                                                     )
                                                                                    )
                                                                                    ),
                                                                                goal(description="S1",
                                                                                     support=evidence(description = "none")),
                                                                                goal(description="S2",
                                                                                     support=evidence(description = "none")),
                                                                                goal(description="S3",
                                                                                     support=evidence(description = "none"))]
                                                              )
                                                              ),
                                                          #Built Binary tree
                                                         goal(description="Build Binary が安全である",
                                                              support=strategy("Produce Built Binaryの安全に必要なものは？",
                                                                               sub_goal11=[goal(description="Vulnarability Data Query Produce Artifactが安全",
                                                                                                support=strategy("Vulnarability Data Queryが安全であるためには？",
                                                                                                                 #Source Code COnsumes Build tree
                                                                                                                 sub_goal12=[goal(description="Source Code Consumes Buildが安全",
                                                                                                                                   support=strategy("Source Code Dependancy Consumesが安全であるためには？",
                                                                                                                                                    sub_goal13=[goal(description="Produce Dependencyが安全",
                                                                                                                                                                        support=strategy("Fetch Produceが安全であるためには？",
                                                                                                                                                                                         sub_goal14=[goal(description="Carries Out Fetchが安全",
                                                                                                                                                                                                          support=strategy("Jfrog Artifactory Carries Outが安全であるためには？",
                                                                                                                                                                                                                         sub_goal15=[goal(description="Uses Jfrog Artifactoryが安全",
                                                                                                                                                                                                                                          support=strategy("Developer Usesが安全であるためには？",
                                                                                                                                                                                                                                                         sub_goal16=[goal(description="P1",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P2",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P3",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P4",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P5",
                                                                                                                                                                                                                                                                           support=evidence(description = "none"))]
                                                                                                                                                                                                                                                          )
                                                                                                                                                                                                                                         ),
                                                                                                                                                                                                                                    goal(description="R1",
                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                      goal(description="R2",
                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                      goal(description="R3",
                                                                                                                                                                                                                                           support=evidence(description = "none"))]
                                                                                                                                                                                                                           )
                                                                                                                                                                                                         ),
                                                                                                                                                                                                     goal(description="S1",
                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                      goal(description="S2",
                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                      goal(description="S3",
                                                                                                                                                                                                           support=evidence(description = "none"))]
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                                goal(description="R1",
                                                                                                                                                                    support=evidence(description = "none")),
                                                                                                                                                                goal(description="R2",
                                                                                                                                                                   support=evidence(description = "none")),
                                                                                                                                                              goal(description="R3",
                                                                                                                                                                   support=evidence(description = "none"))]
                                                                                                                                                    )
                                                                                                                                 ),
                                                                                                                             #Carries Out Build tree
                                                                                                                             goal(description="Carries Out Buildが安全",
                                                                                                                                   support=strategy("Uses Tektlon standard CI/CD pipelineが安全であるためには？",
                                                                                                                                                    sub_goal17=[goal(description="Uses Resourceが安全",
                                                                                                                                                                        support=strategy("CI/CD Controller Usesが安全であるためには？",
                                                                                                                                                                                         sub_goal18=[goal(description="P1",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P2",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P3",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P4",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P5",
                                                                                                                                                                                                          support=evidence(description = "none"))]
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                                goal(description="R1",
                                                                                                                                                                    support=evidence(description = "none")),
                                                                                                                                                                goal(description="R2",
                                                                                                                                                                   support=evidence(description = "none")),
                                                                                                                                                                goal(description="R3",
                                                                                                                                                                   support=evidence(description = "none"))]
                                                                                                                                                    )
                                                                                                                                  ),
                                                                                                                             goal(description="S1",
                                                                                                                                   support=evidence(description = "none")),
                                                                                                                             goal(description="S2",
                                                                                                                                   support=evidence(description = "none")),
                                                                                                                             goal(description="S3",
                                                                                                                                   support=evidence(description = "none"))]
                                                                                                                 )
                                                                                               ),
                                                                                            goal(description="A1",
                                                                                                 support=evidence(description = "none")),
                                                                                            goal(description="A2",
                                                                                                 support=evidence(description = "none")),
                                                                                            goal(description="A3",
                                                                                                 support=evidence(description = "none"))]
                                                                              )
                                                             ),
                                                          #Build Container Image tree
                                                          goal(description="Build Container Image が安全である",
                                                              support=strategy("Produce Built Container imagesの安全に必要なものは？",
                                                                                sub_goal19=[goal(description="Vulnarability Data Query Produce Artifactが安全",
                                                                                                support=strategy("Vulnarability Data Queryが安全であるためには？",
                                                                                                                 #Source Code COnsumes Build tree
                                                                                                                 sub_goal20=[goal(description="Source Code Consumes Buildが安全",
                                                                                                                                   support=strategy("Source Code Dependancy Consumesが安全であるためには？",
                                                                                                                                                    sub_goal21=[goal(description="Produce Dependencyが安全",
                                                                                                                                                                        support=strategy("Fetch Produceが安全であるためには？",
                                                                                                                                                                                         sub_goal22=[goal(description="Carries Out Fetchが安全",
                                                                                                                                                                                                          support=strategy("Jfrog Artifactory Carries Outが安全であるためには？",
                                                                                                                                                                                                                         sub_goal23=[goal(description="Uses Jfrog Artifactoryが安全",
                                                                                                                                                                                                                                          support=strategy("Developer Usesが安全であるためには？",
                                                                                                                                                                                                                                                         sub_goal24=[goal(description="P1",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P2",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P3",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P4",
                                                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                                                      goal(description="P5",
                                                                                                                                                                                                                                                                           support=evidence(description = "none"))]
                                                                                                                                                                                                                                                          )
                                                                                                                                                                                                                                         ),
                                                                                                                                                                                                                                    goal(description="R1",
                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                      goal(description="R2",
                                                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                                                      goal(description="R3",
                                                                                                                                                                                                                                           support=evidence(description = "none"))]
                                                                                                                                                                                                                           )
                                                                                                                                                                                                         ),
                                                                                                                                                                                                     goal(description="S1",
                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                      goal(description="S2",
                                                                                                                                                                                                           support=evidence(description = "none")),
                                                                                                                                                                                                      goal(description="S3",
                                                                                                                                                                                                           support=evidence(description = "none"))]
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                                goal(description="R1",
                                                                                                                                                                    support=evidence(description = "none")),
                                                                                                                                                                goal(description="R2",
                                                                                                                                                                   support=evidence(description = "none")),
                                                                                                                                                              goal(description="R3",
                                                                                                                                                                   support=evidence(description = "none"))]
                                                                                                                                                    )
                                                                                                                                 ),
                                                                                                                             #Carries Out Build tree
                                                                                                                             goal(description="Carries Out Buildが安全",
                                                                                                                                   support=strategy("Uses Tektlon standard CI/CD pipelineが安全であるためには？",
                                                                                                                                                    sub_goal25=[goal(description="Uses Resourceが安全",
                                                                                                                                                                        support=strategy("CI/CD Controller Usesが安全であるためには？",
                                                                                                                                                                                         sub_goal26=[goal(description="P1",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P2",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P3",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P4",
                                                                                                                                                                                                          support=evidence(description = "none")),
                                                                                                                                                                                                     goal(description="P5",
                                                                                                                                                                                                          support=evidence(description = "none"))]
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                                goal(description="R1",
                                                                                                                                                                    support=evidence(description = "none")),
                                                                                                                                                                goal(description="R2",
                                                                                                                                                                   support=evidence(description = "none")),
                                                                                                                                                                goal(description="R3",
                                                                                                                                                                   support=evidence(description = "none"))]
                                                                                                                                                    )
                                                                                                                                  ),
                                                                                                                             goal(description="S1",
                                                                                                                                   support=evidence(description = "none")),
                                                                                                                             goal(description="S2",
                                                                                                                                   support=evidence(description = "none")),
                                                                                                                             goal(description="S3",
                                                                                                                                   support=evidence(description = "none"))]
                                                                                                                 )
                                                                                               ),
                                                                                            goal(description="A1",
                                                                                                 support=evidence(description = "none")),
                                                                                            goal(description="A2",
                                                                                                 support=evidence(description = "none")),
                                                                                            goal(description="A3",
                                                                                                 support=evidence(description = "none"))]
                                                                              )
                                                                      )]
                                                                    )
                                                   )
                                             ),
                                         #Resource Carries Out tree
                                         goal(description="Resources Carries Out Pushが安全である",                                                    
                                              support=strategy(description="Resourceについて分解",
                                                               #AmazonECR tree
                                                               sub_goal27=[goal(description="AmazonECR が安全である",
                                                                               support=strategy(description="Uses AmazonECRが安全であるためには?",
                                                                                                sub_goal28=[goal(description="Uses Resources が安全である",
                                                                                                                support=strategy(description="CI/CD Controller Usesが安全であるためには?",
                                                                                                                                 sub_goal29=[goal(description="P1",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P2",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P3",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P4",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P5",
                                                                                                                                                support=evidence(description = "none"))]
                                                                                                                                 )
                                                                                                                 ),
                                                                                                            goal(description="R1",
                                                                                                                support=evidence(description = "none")),
                                                                                                            goal(description="R2",
                                                                                                                support=evidence(description = "none")),
                                                                                                            goal(description="R3",
                                                                                                                support=evidence(description = "none"))]
                                                                                               )
                                                                               ),
                                                                           #AmazonS3 tree
                                                                           goal(description="AmazonS3 が安全である",
                                                                               support=strategy(description="Uses AmazonS3が安全であるためには?",
                                                                                                sub_goal30=[goal(description="Uses Resources が安全である",
                                                                                                                support=strategy(description="CI/CD Controller Usesが安全であるためには?",
                                                                                                                                 sub_goal31=[goal(description="P1",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P2",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P3",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P4",
                                                                                                                                                support=evidence(description = "none")),
                                                                                                                                             goal(description="P5",
                                                                                                                                                support=evidence(description = "none"))]
                                                                                                                                 )
                                                                                                                 ),
                                                                                                            goal(description="R1",
                                                                                                                support=evidence(description = "none")),
                                                                                                            goal(description="R2",
                                                                                                                support=evidence(description = "none")),
                                                                                                            goal(description="R3",
                                                                                                                support=evidence(description = "none"))]
                                                                                               )
                                                                               )]
                                                              )
                                             ),
                                         goal(description="S1",
                                              support=evidence(description = "none")),
                                         goal(description="S2",
                                              support=evidence(description = "none")),
                                         goal(description="S3",
                                              support=evidence(description = "none"))]
                                  )
                 )
if __name__ == '__main__':
    # n = gsn.pgsn_to_gsn(evidence_class, steps=10000)
    # print(json.dumps(gsn.python_val(n), sort_keys=True, indent=4))
    #print(s('sub_goals').fully_eval())
    SolarWinds = solarwinds.fully_eval()
    pprint.pprint(prettify(SolarWinds))
    # n = gsn.pgsn_to_gsn(SolarWinds, steps=10000)
    # js = json.dumps(gsn.python_val(n), sort_keys=True, indent=4)
    # print(js)
    #