from flask_oauthlib.provider import OAuth2Provider
from main import app
from models import engine, User, Client, Grant, Token
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timedelta


oauth = OAuth2Provider()
oauth.init_app(app)


@oauth.clientgetter
def load_client(client_id):
  with Session(engine) as session:
    client = select(Client).where(client_id=client_id)
  return session.scalar(client)


@oauth.grantgetter
def load_grand(client_id, code):
  with Session(engine) as session:
    grant = select(Grant).where(client_id=client_id, code=code)
  return session.scalar(grant)


@oauth.grantsetter
def save_grant(client_id, code, request, *args, **kwargs):
  expires = datetime.utcnow() + timedelta(seconds=100)
  with Session(engine) as session:
    grant = Grant(client_id=client_id, 
                  code=code['code'],
                  redirect_uri=request.redirect_uri,
                  scope=request.scope,
                  user_id=get_current_user(),
                  expires=expires) 
    session.add(grant)
    session.commit()
  return grant


@oauth.tokengetter
def load_token(access_token=None, refresh_token=None):
  if access_token:
    with Session(engine) as session:
      token = select(Token).where(access_token=access_token)
      return session.scalar(token)
  elif refresh_token:
    with Session(engine) as session:
      token = select(Token).where(refresh_token=refresh_token)
      return session.scalar(token)


@oauth.tokensetter
def save_token(token, request, *args, **kwargs):
  with Session(engine) as session:
    toks = select(Token).where(client_id=request.client.client_id,
                               user_id=request.user.id)
  for t in session.scalars(toks):
    session.delete(t)
  expires_in = token.get('expires_in')
  expires = datetime.utcnow() + timedelta(seconds=expires_in)
  with Session(engine) as session:
    tok = Token(access_token=token["access_token"],
                refresh_token=token["refresh_token"],
                token_type=token["token_type"],
                scope=token["scope"],
                expires=expires,
                client_id=request.client.client_id,
                user_id=request.user.id)
    session.add(tok)
    session.commit()


@oauth.usergetter
def get_user(username, password, *args, **kwargs):
  with Session(engine) as session:
    user = select(User).where(username=username)
  user = session.scalar(user)
  if user:
    return user
  return None 



@app.route('/oauth/token')
@oauth.token_handler
def access_token():
    return None


@app.route('/oauth/token')
@oauth.token_handler
def access_token():
    return {'version': '0.1.0'}


@app.route('/oauth/token', methods=['POST'])
@oauth.token_handler
def access_token():
    return None