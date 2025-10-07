import { Link } from 'react-router-dom';

export default function HomePage() {
  return (
      <body className="min-h-screen bg-[#FFF0F0] text-gray-700">

      <div className=" grid grid-cols-4">
 
        <div className="col-span-1"/>
        <img src="dist/assets/IMG_3974_v1.jpeg" alt="Melissa Cartoon Avatar" className="w-100 h-100 object-contain mt-25 ml-25 col-span-1 shadow-sm"/>


        <div className="col-span-1">
        <h1 className="">
          Senior Data Engineer!!!
        </h1>
        <p className="">
          Under Construction
        </p>
        <div className="col-span-1"/>
</div>
      </div>

    <div className="container mx-auto flex  lg:flex-row p-10">
      <h1 className="flex-col text-3xl font-bold mr-10">Projects</h1>
    {/* <div className='container mx-auto flex flex-col sm:flex-row p-8'> */}
    <h1 className='flex-col text-3xl font-bold'>HELLO</h1></div>
    <div className='container mx-auto flex flex-col sm:flex-row p-8'>
      <Link
        to="/school/login"
        className="inline-block px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
      >
        View Login Demo
      </Link>
    </div>
    <div className='p-8'>
    </div>
    </body>
  );
}