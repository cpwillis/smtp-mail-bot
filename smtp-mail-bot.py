import asyncio
import logging
from aiosmtpd.controller import Controller
from email import message_from_bytes

DOMAIN = "devmailserver.xyz"
HOST = "localhost"
PORT = 25

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MailHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        # Check recipient domain validity
        if not (recipient := address.split("@")[-1]) == DOMAIN:
            logger.error(f"Invalid recipient domain: {recipient}")
            return "550"
        envelope.rcpt_tos.append(address)
        return "250"

    async def handle_DATA(self, server, session, envelope):
        # Extract sender and recipients
        sender = envelope.mail_from
        recipients = envelope.rcpt_tos
        logger.info(f"Mail received from {sender} to {recipients}")

        # Extract plain text content
        if plain_text_part := self.extract_plain_text(envelope.content):
            logger.info(f"Plain text content:\n{plain_text_part}")

        logger.info("End of message")
        return "250"

    def extract_plain_text(self, content):
        email_message = message_from_bytes(content)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode("utf-8")
        return None


if __name__ == "__main__":
    # Start SMTP server
    controller = Controller(MailHandler(), hostname=HOST, port=PORT)
    logger.info(f"Starting SMTP server at {HOST}:{PORT}...")
    controller.start()
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()
