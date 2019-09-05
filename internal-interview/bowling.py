class BowlingGame(object):
    def __init__(self):
        self.min_roll = 0
        self.max_roll = 10

        self.rolls = []
        self.strike_indexes = []
        self.spare_indexes = []
        self.current_roll_index = 0
        self.current_frame_remaining = self.max_roll
        self.current_frame_rolls = []
        self.frames_completed = 0

    def roll(self, pins):

        if self.frames_completed == 10:
            raise IndexError("10 frames completed. No more rolling allowed.")

        if pins < self.min_roll:
            raise ValueError("Can't roll less than {}".format(self.min_roll))

        if pins > self.max_roll:
            raise ValueError("Can't roll more than {}".format(self.max_roll))

        if pins > self.current_frame_remaining:
            raise ValueError("Not enough pins remaining to support roll")

        # Track this roll.
        self.rolls.append(pins)
        self.current_frame_rolls.append(pins)
        self.current_frame_remaining -= pins
        self.current_roll_index = len(self.rolls) - 1

        frame_rolls = len(self.current_frame_rolls)

        if self.frames_completed == 9:

            # Deal with 10th frame separately, no bonus scoring.
            if frame_rolls == 1:  # First roll
                if self.current_frame_remaining == 0:
                    # strike on first roll, frame NOT complete.
                    self.current_frame_remaining = self.max_roll
            elif frame_rolls == 2:  # Second roll
                if self.current_frame_remaining == 0:
                    # second strike or spare, frame NOT complete.
                    self.current_frame_remaining = self.max_roll
                else:
                    if self.current_frame_rolls[0] != 10:
                        # First frame wasn't a strike, so, since this frame didn't make a spare, we are done.
                        self.frames_completed += 1
            else:  # Third roll, done no matter what.
                self.frames_completed += 1

        else:
            # Frames 1-9 ... so, normal rules.
            if (self.current_frame_remaining == 0) or (frame_rolls == 2):

                # Frame complete.
                self.frames_completed += 1

                # Record for scoring.
                if self.current_frame_remaining == 0:
                    # Strike or spare
                    if frame_rolls == 1:
                        self.strike_indexes.append(self.current_roll_index)
                    else:
                        self.spare_indexes.append(self.current_roll_index)

                # Reset for next frame.
                self.current_frame_rolls = []
                self.current_frame_remaining = self.max_roll

    def score(self):

        if self.frames_completed != 10:
            raise IndexError("Cannot score incomplete game.")

        for strike in self.strike_indexes:
            # extra +1 because slices are exclusive
            value = sum(self.rolls[strike:strike+3])
            self.rolls[strike] = value

        for spare in self.spare_indexes:
            # extra +1 because slices are exclusive.
            value = sum(self.rolls[spare-1:spare+2])
            self.rolls[spare] = value
            self.rolls[spare - 1] = 0

        return sum(self.rolls)
