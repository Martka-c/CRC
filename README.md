# CRC

## Deploy na cloud run
1. Otwieramy konsolę - musimy mieć zainstalowanego gclouda 
2. gcloud init 
3. Potrzebne role: roles/run.admin, roles/iam.serviceAccountUser, roles/logging.viewer

4. gcloud run deploy
5. Powinno się zakończyć errorem 

6. compute uruchamia się za pomocą konta serwisowego - "compute" w nazwie, trzeba mu nadać uprawnienie Cloud Build Service Account

7. Pamiętamy w jakiej lokalizacji deployowaliśmy apkę, bo będzie to potrzebne 
8. gcloud run deploy

9. gcloud run services add-iam-policy-binding pierwsza-apka \
  --member=allUsers \
  --role=roles/run.invoker \
  --region=europe-west2

APKA JEST PUBLICZNIE DOSTĘPNA, SPRAWDŹ TELEFON

## Cloud 