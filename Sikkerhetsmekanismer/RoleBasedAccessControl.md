For å iverksette Role Based Access Control til en Job i Kubernetes vil du trenge en Service Account for å binde RBAC-reglene til Job'en 
Et eksempel på en slik Service Account er laget i job-SA.yaml
En RBAC settes opp ved å lage en Role som inneholder hvilke rettigheter en skal ha tilgjengelig, og en Role Binding som knytter rettighetene til et Namespace (i dette tilfellet).
Role er laget i job-role.yaml
RoleBinding er laget i job-rolebinding.yaml

