import { FC } from 'react';

interface Props {
  prompt: string;
  linkText: string;
  href: string;
}

const FooterLinks: FC<Props> = ({ prompt, linkText, href }) => (
  <p className="text-sm text-center mt-4">
    {prompt}{' '}
    <a href={href} className="text-indigo-600 hover:underline">
      {linkText}
    </a>
  </p>
);

export default FooterLinks;