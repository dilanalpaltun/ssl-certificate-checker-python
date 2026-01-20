from ssl_checker import CertificateChecker


def main():
    hostname = input("Enter domain (example.com): ").strip()

    if not hostname:
        print("No domain provided.")
        return

    checker = CertificateChecker()
    print(checker.check_certificate(hostname))


if __name__ == "__main__":
    main()
