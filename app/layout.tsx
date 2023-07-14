import './globals.css'

export const metadata = {
  title: 'Questions',
  description: 'Hello World',
}


export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className='h-full'>
      <body className='h-full p-3 flex items-center justify-center bg-black text-white'>{children}</body>
    </html>
  )
}
