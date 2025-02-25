from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="Test@test.test", password="test")
        self.habit = Habit.objects.create(
            owner=self.user,
            place_of_event="Home",
            time_of_event="10:00:00",
            habit="Зарядка",
            reward="чашка кофе",
            time_to_complete=40,
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_retrieve(self):
        url = reverse("habits:habit-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place_of_event"), self.habit.place_of_event)

    def test_habits_create(self):
        url = reverse("habits:habit-create")
        data = {
            "owner": self.user.pk,
            "place_of_event": "Home",
            "time_of_event": "10:00",
            "habit": "Зарядка",
            "time_to_complete": 40,
            "reward": "чашка кофе",
        }
        response = self.client.post(url, data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habits_update(self):
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {
            "place_of_event": "Work",
        }
        response = self.client.patch(url, data)
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.get(pk=self.habit.pk).place_of_event, "Work")

    def test_habits_delete(self):
        url = reverse("habits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habits_list(self):
        url = reverse(
            "habits:habits",
        )
        response = self.client.get(url)
        data = response.status_code
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
