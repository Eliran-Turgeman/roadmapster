from pydantic import ValidationError

from generation.base_roadmap_generator import BaseRoadmapGenerator
from generation.roadmap_models import Roadmap


class RoadmapGenerator(BaseRoadmapGenerator):
    def generate(self, roadmap_topic: str) -> Roadmap:
        roadmap_json_mock = {
            "nodes": [
                {
                    "id": "basic_concepts",
                    "title": "Basic Concepts",
                    "description": "Learn the fundamental concepts of Kubernetes, including pods, deployments, and services.",
                    "resources": [
                        {
                            "name": "Kubernetes Basics",
                            "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/"
                        },
                        {
                            "name": "Kubernetes 101 - YouTube",
                            "url": "https://www.youtube.com/watch?v=s_o8dwzRlu4"
                        }
                    ],
                    "status": "required",
                    "prerequisites": []
                },
                {
                    "id": "setup_local_env",
                    "title": "Setup Local Environment",
                    "description": "Set up a local Kubernetes development environment with Minikube.",
                    "resources": [
                        {
                            "name": "Install Minikube",
                            "url": "https://minikube.sigs.k8s.io/docs/start/"
                        }
                    ],
                    "status": "required",
                    "prerequisites": ["basic_concepts"]
                },
                {
                    "id": "core_components",
                    "title": "Core Components",
                    "description": "Understand the core components of Kubernetes such as etcd, API server, scheduler, controllers, and more.",
                    "resources": [
                        {
                            "name": "Cluster Architecture",
                            "url": "https://kubernetes.io/docs/concepts/overview/components/"
                        }
                    ],
                    "status": "required",
                    "prerequisites": ["setup_local_env"]
                },
                {
                    "id": "workload_management",
                    "title": "Workload Management",
                    "description": "Learn to manage workloads, roll out updates, and scale applications.",
                    "resources": [
                        {
                            "name": "Deployments",
                            "url": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"
                        }
                    ],
                    "status": "required",
                    "prerequisites": ["core_components"]
                },
                {
                    "id": "networking",
                    "title": "Networking",
                    "description": "Explore how networking functions in Kubernetes and how to set up cluster networking.",
                    "resources": [
                        {
                            "name": "Cluster Networking",
                            "url": "https://kubernetes.io/docs/concepts/cluster-administration/networking/"
                        }
                    ],
                    "status": "required",
                    "prerequisites": ["workload_management"]
                },
                {
                    "id": "storage",
                    "title": "Storage",
                    "description": "Understand persistent storage in Kubernetes and how to implement it.",
                    "resources": [
                        {
                            "name": "Storage Classes",
                            "url": "https://kubernetes.io/docs/concepts/storage/storage-classes/"
                        }
                    ],
                    "status": "optional",
                    "prerequisites": ["workload_management"]
                },
                {
                    "id": "security",
                    "title": "Security",
                    "description": "Learn best practices for securing Kubernetes clusters and applications.",
                    "resources": [
                        {
                            "name": "Kubernetes Security",
                            "url": "https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/"
                        }
                    ],
                    "status": "required",
                    "prerequisites": ["networking"]
                },
                {
                    "id": "observability",
                    "title": "Observability",
                    "description": "Learn about monitoring, logging, and debugging applications in Kubernetes.",
                    "resources": [
                        {
                            "name": "Monitoring and Logging",
                            "url": "https://kubernetes.io/docs/tasks/debug-application-cluster/"
                        }
                    ],
                    "status": "optional",
                    "prerequisites": ["workload_management"]
                },
                {
                    "id": "ci_cd_integration",
                    "title": "CI/CD Integration",
                    "description": "Learn how to integrate Kubernetes with CI/CD systems for automated deployment workflows.",
                    "resources": [
                        {
                            "name": "CI/CD with Kubernetes",
                            "url": "https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/"
                        }
                    ],
                    "status": "optional",
                    "prerequisites": ["core_components", "workload_management"]
                }
            ]
        }

        try:
            return Roadmap(**roadmap_json_mock)
        except ValidationError as e:
            print(f'failed to serialize invalid roadmap, error={e}')

        return Roadmap(nodes=[])
