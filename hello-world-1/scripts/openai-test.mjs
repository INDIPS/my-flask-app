import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://aihubmix.com/v1',
  apiKey: '<AIHUBMIX_API_KEY>',
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [
      {
        role: 'user',
        content: 'What is the meaning of life?',
      },
    ],
  });

  console.log(completion.choices[0].message);
}

main();
