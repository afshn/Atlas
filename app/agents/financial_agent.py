from datetime import datetime

from app.models.memory import Memory


class AtlasParser:

    def parse(self, text):

        memory = Memory(

            text=text,

            created_at=datetime.now()

        )

        self.detect(memory)

        return memory

    def detect(self, memory):

        text = memory.text

        people = [

            "ویونا",

            "علی",

            "رضا",

            "محمد"

        ]

        for person in people:

            if person in text:

                memory.entities.append(person)

        if "ارسال" in text:

            memory.action = "ارسال"

            memory.follow_up = True

        if "خرید" in text:

            memory.action = "خرید"

        if "فروش" in text:

            memory.action = "فروش"

        if "چای" in text:

            memory.tags.append("چای")

        if "هزینه" in text:

            memory.category = "هزینه"

        elif "درآمد" in text:

            memory.category = "درآمد"

        else:

            memory.category = "رویداد"

        if memory.follow_up:

            memory.importance = 4