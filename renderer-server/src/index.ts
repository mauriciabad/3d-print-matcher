import fs from 'fs'
import puppeteer from 'puppeteer'
import models, { Model } from './data/models'
//
;(async () => {
  console.log('Starting...')

  const browser = await puppeteer.launch()

  const page = await browser.newPage()
  printConsole(page)
  await page.setViewport({ width: 1024, height: 1024 })

  for (const model of models) {
    // const pageHTML = fs
    //   .readFileSync('./src/index.html', 'utf8')
    //   .replace(
    //     'const model = INJECTED_MODEL_DATA_GOES_HERE',
    //     `const model = ${JSON.stringify(model)}`
    //   )
    // await page.goto(`file://${__dirname}/pages/test.html`)

    // await page.setContent(pageHTML)

    await page.goto(`http://localhost:5000`)

    await wait(1000)
    await page.screenshot({
      path: screenshotPath(model),
    })
    console.log(`Created ${screenshotPath(model)}`)
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

function screenshotPath(model: Model): string {
  return `./out/${model.name}.jpg`
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
