# WS1A - Secure your web service

### BYOD Requirements
This workshop requires that you bring your own laptop. Please have the prerequisities installed before you attend the workshop.

### Prerequisites
- Terminal with the ability to SSH
- Docker for Mac or Docker for Windows via https://docs.docker.com/install/#desktop
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Web browser (Firefox or Chrome recommended)
- **Bonus**: Install Go and setup Go workspace, [instructions here](https://golang.org/doc/code.html) *(Not required)*

### Objectives
- Deploy Docker container with [Nginx](https://certbot.eff.org/)
- Deploy Docker container with [Certbot](https://github.com/certbot/certbot)
- Use Certbot to register with [Let's Encrypt](https://letsencrypt.org/) and get an SSL certificate
- Setup automation to schedule renewals for your certificate
- Adjust Nginx TLS settings to improve security posture
- **Bonus**: Deploy Docker container with Go app that uses the [ACME autocert package](https://godoc.org/golang.org/x/crypto/acme/autocert) to get a cert and keep it renewed *(Not required)*
