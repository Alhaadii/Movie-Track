<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-8">
    <div
      class="flex justify-center items-center flex-col gap-y-4 md:max-w-lg mx-auto p-8 bg-gray-300 shadow-lg rounded-md lg:max-w-2xl"
    >
      <div>
        <h1 class="font-bold text-5xl">AQUAMAN</h1>
      </div>
      <div class="w-96 flex justify-between items-center">
        <div class="">
          <h1 class="font-bold uppercase">Director name</h1>
          <h1 class="uppercase text-gray-700">Gorider</h1>
        </div>
        <div class="">
          <h1 class="font-bold uppercase">Release date</h1>
          <h1 class="uppercase text-gray-700">2021</h1>
        </div>
      </div>

      <!-- checking to the Second page -->
      <div v-if="currentStep === 0">
        <div class="">
          <img
            class="h-full w-full object-cover"
            src="https://source.boomplaymusic.com/buzzgroup2/M00/37/DE/rBEeJGKxjXyAfuaLAALDc3CS9iQ25.jpeg"
            alt=""
            srcset=""
          />
        </div>
        <div class="text-center">
          <button
            @click="currentStep++"
            class="bg-gray-900 p-4 mt-5 text-white rounded-md hover:bg-gray-800"
          >
            Book Tickets
          </button>
        </div>
        <section>
          <h1 class="font-bold uppercase mb-4">Synopsis</h1>
          <p class="max-w-md text-gray-600">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae quam
            maxime nemo dolorem nisi nostrum, numquam dicta quisquam earum vitae
            illo molestias reprehenderit perferendis cumque fugit molestiae
            adipisci eveniet facilis tempore animi. Iste porro commodi deleniti,
            beatae ut earum autem.
          </p>
        </section>
      </div>

      <!-- Second page with Go Back -->
      <div v-else-if="currentStep === 1">
        <div class="font-bold uppercase w-96">
          <h1 class="text-left">How many Seats?</h1>
          <div class="flex flex-col w-full space-y-2 mt-4">
            <button
              :class="[
                'p-4 text-white rounded-md',
                bookingData.numberOfSeats === index
                  ? 'bg-gray-900'
                  : 'bg-gray-700',
              ]"
              v-for="index in 8"
              @click="setNumberOfSeats(index)"
            >
              {{ index }}
            </button>
          </div>
        </div>
      </div>

      <!-- Third page with Go Back -->
      <div v-else-if="currentStep === 2" class="">
        <div class="font-medium uppercase w-96">
          <h1 class="text-left">DATE</h1>
          <input
            type="date"
            class="p-2 cursor-pointer w-full mt-4 rounded-md"
            v-model="bookingData.date"
          />
        </div>
        <div class="flex flex-col space-y-4">
          <h1 class="font-medium text-xl text-black mt-7 uppercase">
            Cinema & Show
          </h1>
          <div class="">
            <div class="bg-white shadow-xl p-4 rounded-md">
              <h3 class="font-bold text-sm text-gray-800">Mugadisho theatre</h3>
              <div class="space-x-2">
                <button class="outline outline-gray-100 p-1 mt-2">
                  12:30PM
                </button>
                <button class="outline outline-gray-100 p-1 mt-2">
                  3:30PM
                </button>
              </div>
            </div>
            <div class="bg-white shadow-xl p-4 rounded-md mt-2">
              <h3 class="font-bold text-sm text-gray-800">Kismayu Theatre</h3>
              <div class="space-x-2">
                <button class="outline outline-gray-100 p-1 mt-2">
                  12:30PM
                </button>
                <button class="outline outline-gray-100 p-1 mt-2">
                  3:30PM
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Fourth Page with Go Back -->
      <div v-else-if="currentStep === 3" class="">
        <div class="w-96">
          <h1 class="font-medium text-2xl">Select Seats</h1>
          <div class="">
            <div
              class="flex flex-row"
              :key="row"
              v-for="row in Object.keys(seatStructure)"
            >
              <span
                @click="selectSeat(row, seat[0])"
                v-for="seat in seatStructure[row]"
                class="w-6 h-8 m-2 rounded-[2px]"
                :class="
                  seat[1] === 'Available'
                    ? 'bg-blue-300'
                    : seat[1] === 'Selected'
                    ? 'bg-blue-600'
                    : 'bg-gray-200'
                "
              >
              </span>
            </div>
          </div>
        </div>
      </div>

      <div v-else-if="currentStep === 4" class="">
        <h1 class="text-center text-9xl">🍿</h1>
        <h2 class="mt-4 text-center font-bold uppercase">Enjoy The Movie!</h2>
      </div>

      <!-- Button to manage pages -->
      <div class="flex justify-between w-full">
        <button
          class="bg-gray-900 p-4 mt-5 text-white rounded-md hover:bg-gray-800"
          v-if="currentStep !== 0"
          @click="currentStep--"
        >
          Go Back
        </button>
        <button
          class="bg-gray-900 p-4 mt-5 text-white rounded-md hover:bg-gray-800"
          v-if="currentStep !== 0"
          @click="currentStep++"
        >
          NEXT
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

function getSeatStructure(alphabets, numbers) {
  const structure = {}
  for (const alphabet of alphabets) {
    structure[alphabet] = []
    for (const number in numbers) {
      structure[alphabet].push([number, 'Available'])
    }
  }
  return structure
}

const seatStructure = reactive(
  getSeatStructure(['A', 'B', 'C', 'D', 'E'], [1, 2, 3, 4, 5, 6, 7, 8])
)

const today = new Date().toISOString().substr(0, 10)
const currentStep = ref(1)

const bookingData = reactive({
  numberOfSeats: 0,
  selctedSeats: [],
  date: today,
})

function setNumberOfSeats(seat) {
  bookingData.numberOfSeats = seat
}

function selectSeat(row, number) {
  const seat = seatStructure[row].find((seat) => seat[0] === number)
  seat[1] = 'Selected'

  bookingData.selctedSeats.push(`${row}${number}`)
}
</script>
