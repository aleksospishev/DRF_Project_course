from rest_framework.validators import ValidationError


class HabitValidator:
    # def __init__(self, reward, related_habit, nice_habit):
    #     self.reward = reward
    #     self.related_habit = related_habit
    #     self.nice_habit = nice_habit
    #
    # def __call__(self, obj):
    #     reward_obj = obj.get(self.reward)
    #     related_habit_obj = obj.get(self.related_habit)
    #     nice_habit_obj = obj.get(self.nice_habit)
    #
    #
    #     if reward_obj and related_habit_obj:
    #         raise ValidationError("Может быть заполнено только одно поле ")
    #
    #     if nice_habit_obj:
    #         if related_habit_obj or reward_obj:
    #             raise ValidationError(
    #                 "У приятной привычки не может быть связаной_ привычки или награды"
    #             )
    #     else:
    #         if not reward_obj and not related_habit_obj:
    #             raise ValidationError(
    #                 "У полезной привычки Должна быть или награда или связанная приятная привычка"
    #             )
    #     if related_habit_obj:
    #         if not related_habit_obj.nice_habit:
    #             raise ValidationError(
    #                 "Связаная привычка должна быть приятной привычкой"
    #             )
    def __init__(self, value):
        self.value = value

    def __call__(self, value):
        if value["reward"] and value["related_habit"]:
            if value["reward"] and value["related_habit"]:
                raise ValidationError("Может быть заполнено только одно поле ")

            if value["nice_habit"]:
                if value["related_habit"] or value["reward"]:
                    raise ValidationError(
                        "У приятной привычки не может быть связаной_ привычки или награды"
                    )
            else:
                if not value["reward"] and not value["related_habit"]:
                    raise ValidationError(
                        "У полезной привычки Должна быть или награда или связанная приятная привычка"
                    )
            if value["related_habit"]:
                if not value["related_habit"]["nice_habit"]:
                    raise ValidationError(
                        "Связаная привычка должна быть приятной привычкой"
                    )
