from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций работ.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            image="Job №1 image path",
            description="Job №1 description",
            content="Job №1 content. " * 100,
        )

    def test_job_content_creation(self) -> None:
        """
        Тестирование моделей сообщений для блога.

        :return:
        """

        job = Job.objects.get(description="Job №1 description")

        content = "Job №1 content. " * 100
        self.assertEqual(job.summary(), content[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
