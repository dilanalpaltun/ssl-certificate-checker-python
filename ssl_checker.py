import socket
import ssl
from datetime import datetime


class CertificateChecker:
    def __init__(self, port: int = 443):
        self.port = port

    def check_certificate(self, hostname: str) -> str:
        """
        Connects to a host and retrieves SSL certificate details.
        Returns: validity, expiry date, issuer, subject.
        """
        try:
            sock = socket.create_connection((hostname, self.port), timeout=8)
            context = ssl.create_default_context()
            wrapped_sock = context.wrap_socket(sock, server_hostname=hostname)

            cert = wrapped_sock.getpeercert()
            wrapped_sock.close()
            sock.close()

            if not cert:
                return "Certificate could not be retrieved."

            not_after = cert.get("notAfter")
            if not not_after:
                return "Certificate retrieved, but expiry date is missing."

            expiry_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y GMT")
            now = datetime.utcnow()

            if expiry_date < now:
                result = "Status: EXPIRED"
            else:
                result = "Status: VALID"

            result += f"\nValid until (UTC): {expiry_date}"

            issuer = dict(x[0] for x in cert.get("issuer", []))
            subject = dict(x[0] for x in cert.get("subject", []))

            result += f"\nIssuer (organizationName): {issuer.get('organizationName')}"
            result += f"\nSubject (commonName): {subject.get('commonName')}"

            return result

        except ssl.SSLCertVerificationError as err:
            return f"SSL verification failed: {err}"
        except Exception as err:
            return f"Connection failed: {err}"
