from textwrap import dedent

from pm.vtt2txt import vtt_to_text


def test_simple_vtt_file():
    vtt_text = dedent("""\
        WEBVTT

        00:00.000 --> 00:04.480
        Let's talk about fixing circular imports in Python.

        00:04.480 --> 00:07.280
        We have a Django application here called

        00:07.280 --> 00:11.240
        users which has a tasks module within it that contains Celery tasks.

        00:11.240 --> 00:13.840
        Celery tasks are typically run in the background.

        00:13.840 --> 00:17.460
        For example, here, we're sending a welcome email to a user.
    """)
    assert vtt_to_text(vtt_text) == dedent("""\
        Let's talk about fixing circular imports in Python.
        We have a Django application here called users which has a tasks module within it that contains Celery tasks.
        Celery tasks are typically run in the background.
        For example, here, we're sending a welcome email to a user.
    """.rstrip())
