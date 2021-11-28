import fs from 'fs'
import puppeteer from 'puppeteer'
import models, { Model } from './data/models'

const rotations: number[] = [0, 90, 180, 270]
const cameraLocations: Point[] = [
  { x: 0, y: 0, z: -1 },
  { x: 0, y: 0, z: 1 },
  { x: 0, y: -1, z: 0 },
  { x: 0, y: 1, z: 0 },
  { x: -1, y: 0, z: 0 },
  { x: 1, y: 0, z: 0 },
]

interface Point {
  x: number
  y: number
  z: number
}

//
;(async () => {
  console.log('Starting...')

  const browser = await puppeteer.launch()

  const page = await browser.newPage()
  // printConsole(page)
  await page.setViewport({ width: 1024, height: 1024 })

  for (const model of models) {
    for (const cameraLocation of cameraLocations) {
      const pageHTML = fs.readFileSync('./src/index.html', 'utf8').replace(
        'const modelData = INJECTED_MODEL_DATA_GOES_HERE',
        `const modelData = ${JSON.stringify({
          ...model,
          cameraLocation,
        })}`
      )
      fs.writeFileSync('./src/temp.html', pageHTML)

      await page.goto(`http://localhost:5000/temp`)

      await wait(1000)

      const screenshotName = screenshotPath(model, cameraLocation)
      await page.screenshot({
        path: screenshotName,
      })

      console.log(`Created ${screenshotName}`)
    }
  }

  await browser.close()

  console.log('Done!')
})()

function wait(ms: number): Promise<void> {
  return new Promise((resolve) =>
    setTimeout(() => {
      resolve(undefined)
    }, ms)
  )
}

function screenshotPath(model: Model, cameraLocation: Point): string {
  return `./out/${model.name}_${cameraLocation.x}_${cameraLocation.y}_${cameraLocation.z}.jpg`
}

function printConsole(page: puppeteer.Page): void {
  page
    .on('console', (message) =>
      console.log(
        `${message.type().substr(0, 3).toUpperCase()} ${message.text()}`
      )
    )
    .on('pageerror', ({ message }) => console.log(message))
    .on('response', (response) =>
      console.log(`${response.status()} ${response.url()}`)
    )
    .on('requestfailed', (request) =>
      console.log(`${request.failure().errorText} ${request.url()}`)
    )
}
